import pandas as pd
import pyodbc
import sqlalchemy
from sqlalchemy import create_engine, text

# Настройки подключения (замените на свои)
SERVER = 'YOUR_SERVER_NAME'
DATABASE = 'BelleCroissantLyonnaisBI'
USERNAME = 'YOUR_USERNAME'
PASSWORD = 'YOUR_PASSWORD'
DRIVER = '{ODBC Driver 17 for SQL Server}'

# Формирование строки подключения
conn_str = f'mssql+pyodbc://{USERNAME}:{PASSWORD}@{SERVER}/{DATABASE}?driver={DRIVER}'
engine = create_engine(conn_str)

def create_tables():
    """Создание таблиц в базе данных согласно схеме."""
    create_queries = [
        """CREATE TABLE Customers (
            CustomerID INT IDENTITY(1,1) PRIMARY KEY,
            Name NVARCHAR(100),
            Email NVARCHAR(100),
            Phone NVARCHAR(20),
            JoinDate DATE
        );""",
        """CREATE TABLE CustomerFeedback (
            FeedbackID INT IDENTITY(1,1) PRIMARY KEY,
            CustomerID INT,
            Date DATE,
            Rating INT,
            Comment NVARCHAR(MAX),
            FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
        );""",
        """CREATE TABLE SocialMediaEngagement (
            PostID INT IDENTITY(1,1) PRIMARY KEY,
            Date DATE,
            Platform NVARCHAR(50),
            Likes INT,
            Shares INT,
            Comments INT
        );""",
        """CREATE TABLE WebsiteAnalytics (
            VisitID INT IDENTITY(1,1) PRIMARY KEY,
            Date DATE,
            Page NVARCHAR(100),
            Pageviews INT
        );""",
        """CREATE TABLE LoyaltyProgramHistory (
            TransactionID INT IDENTITY(1,1) PRIMARY KEY,
            CustomerID INT,
            TransactionDate DATE,
            PointsEarned INT,
            PointsRedeemed INT,
            Level NVARCHAR(50),
            FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
        );"""
    ]
    
    with engine.connect() as conn:
        for query in create_queries:
            try:
                conn.execute(text(query))
                print(f"Таблица создана или уже существует.")
            except Exception as e:
                print(f"Ошибка при создании таблицы: {e}")

def import_data():
    """Импорт данных из CSV файлов в соответствующие таблицы."""
    files = {
        'customers_data.csv': 'Customers',
        'customer_feedback.csv': 'CustomerFeedback',
        'social_media_engagement.csv': 'SocialMediaEngagement',
        'website_analytics.csv': 'WebsiteAnalytics',
        'loyalty_program_history.csv': 'LoyaltyProgramHistory'
    }
    
    for file, table_name in files.items():
        try:
            df = pd.read_csv(file)
            df.to_sql(table_name, engine, if_exists='append', index=False)
            print(f"Данные из {file} успешно импортированы в {table_name}.")
        except FileNotFoundError:
            print(f"Файл {file} не найден.")
        except Exception as e:
            print(f"Ошибка при импорте {file}: {e}")

if __name__ == "__main__":
    create_tables()
    import_data()

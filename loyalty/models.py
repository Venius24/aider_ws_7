from django.db import models

class LoyaltyTransaction(models.Model):
    points_earned = models.IntegerField(default=0)
    points_redeemed = models.IntegerField(default=0)
    transaction_date = models.DateField()
    customer_id = models.IntegerField() # Assuming simple ID for now

    def __str__(self):
        return f"Transaction on {self.transaction_date}"

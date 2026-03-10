from django.db import models
from customers.models import Customer

class Feedback(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    comment = models.TextField()
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    date = models.DateField()
    sentiment = models.CharField(max_length=10, blank=True) # Positive, Negative, Neutral

    def __str__(self):
        return f"{self.customer.name} - {self.rating}"

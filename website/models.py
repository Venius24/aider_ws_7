from django.db import models

class WebPage(models.Model):
    page_name = models.CharField(max_length=100)
    pageviews = models.IntegerField(default=0)
    date = models.DateField()

    def __str__(self):
        return self.page_name

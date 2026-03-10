from django.db import models

class SocialMediaPost(models.Model):
    platform = models.CharField(max_length=50)
    likes = models.IntegerField(default=0)
    shares = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)
    date = models.DateField()

    def __str__(self):
        return f"{self.platform} - {self.date}"

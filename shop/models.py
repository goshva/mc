from django.conf import settings
from django.db import models
from django.utils import timezone

class Good(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    discription = models.CharField(max_length=300)
    text = models.TextField()
    kind = models.CharField(max_length=300)
    name = models.CharField(max_length=200)
    photo_url = models.CharField(max_length=1000)
    article = models.CharField(max_length=20)
    color = models.CharField(max_length=250)
    price_5k = models.FloatField()
    price_10k = models.FloatField()
    price_20k = models.FloatField()
    price_many = models.FloatField()
    size = models.FloatField()
    weight = models.FloatField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

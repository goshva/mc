from django.conf import settings
from django.db import models
from django.utils import timezone

class images(models.Model):
    id_no=models.IntegerField()
    name=models.CharField(max_length=20)  
    loc=models.CharField(max_length=20)    
    image=models.ImageField(upload_to='images')   
    
 
    def __str__(self):        
        return self.name
        
class Good(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    discription = models.CharField(max_length=300)
    text = models.TextField()
    kind = models.CharField(max_length=300)
    name = models.CharField(max_length=200)
    photo_url = models.CharField(max_length=3000,null=True)
    image= models.ImageField(upload_to='uploads/products/',null=True)
    article = models.CharField(max_length=20)
    color = models.CharField(max_length=250)
    price_5k = models.FloatField(blank=True,null=True)
    price_10k = models.FloatField(blank=True,null=True)
    price_20k = models.FloatField(blank=True,null=True)
    price_many = models.FloatField(blank=True,null=True)
    size = models.FloatField(blank=True,null=True)
    weight = models.FloatField(blank=True,null=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

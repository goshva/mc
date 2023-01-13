from django.contrib import admin
from .models import Good
from .models import images   
class AdminImages(admin.ModelAdmin):    
    list_display = ['id_no','name','loc','image'] 

admin.site.register(images,AdminImages)
admin.site.register(Good)

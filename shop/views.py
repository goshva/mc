from django.shortcuts import render
from .models import Good

def goods_list(request):
    goods = Good.objects.order_by('published_date')
    return render(request, 'goods_list.html', {'goods': goods})

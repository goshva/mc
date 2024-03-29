from django.shortcuts import render , redirect , HttpResponseRedirect
from store.models.product import Products
from store.models.category import Category
from django.views import View
from django.http import JsonResponse
import json


# Create your views here.
class Index(View):

    def post(self , request):
    #     product = request.POST.get('product')
    #     remove = request.POST.get('remove')
    #     add = request.POST.get('add')
    #     fixed = request.POST.get('fixed')
        cart = request.session.get('cart')

    #     print(product)
        
    #     if cart:
    #         quantity = cart.get(product)
    #         if quantity:
    #             if fixed:
    #                 if remove:
    #                     if quantity<=1 or (quantity - int(fixed)) < 1:
    #                         cart.pop(product)
    #                     else:
    #                         cart[product] = quantity - int(fixed)
    #                 if add:
    #                         cart[product]  = quantity+int(fixed)
    #         else:
    #             cart[product] = 1
    #     else:
    #         cart = {}
    #         cart[product] = 1
    #     request.session['cart'] = cart
    #     print('cart' , request.session['cart'])
    #     return redirect('homepage')




    def get(self , request):
        # print()
        return HttpResponseRedirect(f'/store{request.get_full_path()[1:]}')

def store(request):
    
    cart = request.session.get('cart')
    if not cart:
        request.session['cart'] = {}
    products = None
    categories = Category.get_all_categories()
    categoryID = request.GET.get('category')
    if categoryID:
        products = Products.get_all_products_by_categoryid(categoryID)
    else:
        products = Products.get_all_products();

    data = {}
    data['products'] = products
    data['categories'] = categories

    print('you are : ', request.session.get('email'))
    return render(request, 'index.html', data)



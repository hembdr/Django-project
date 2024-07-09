from django.shortcuts import render
from catalog.models import Category
# Create your views here.

def product_form(request):
    if request.method=="POST":   
        name=request.POST['name']  
        obj = Category(name=__name__)
        obj.save()
    else:
        print(request.method)
    return render(request,'index.html')
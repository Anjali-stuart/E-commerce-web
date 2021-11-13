from django.shortcuts import render,HttpResponse
from .models import Product, Introduction
from .forms import StuForm
from math import ceil
# Create your views here.
def index(request):
    products = Product.objects.all()
    print("hi this is working ")
    print("products", products)
    n = len(products)
    # nslides = n//4+ceil((n/4)-(n//4))

    return render(request, 'shop/index.html',{"products":products})

def about(request):
    # return HttpResponse("this is about us")

    return render(request, 'shop/about.html')
def data(request):
    a = Product.objects.all()
    # print("type " , type(a))
    # print('Hi ')
    # for i in a:
    #     print(i)

    return render(request, 'shop/index.html', {"produts": a})

def contact(request):
    # if request.method=="POST":
    #     st = StuForm(request.POST)
    #     if st.is_valid():
    #         return HttpResponse("thanks")
    # else:
    #     form = StuForm()
    return render(request, 'shop/contact.html')

def search(request):
    return HttpResponse("this is search")

    # return render(request, 'shop/index.html')

def productView(request):
    return HttpResponse("this is productView")

    # return render(request, 'shop/index.html')

def checkout(request):
    return HttpResponse("this is checkout")
    # return render(request, 'shop/index.html')

def tracker(request):
    return HttpResponse("this is tracker")

    # return render(request, 'shop/index.html')

def introduction(request):
    a = Introduction.objects.all()
    for i in a:
        print(a)

    return render(request, 'shop/contact.html', {"details":a})


def terms(request):
    return render(request, 'shop/djangoTerms.html')
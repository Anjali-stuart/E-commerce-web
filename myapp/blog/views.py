from django.shortcuts import render ,HttpResponse

# Create your views here.
def index(request):
    return render(request,'blog/index.html')

def about(request):
    return HttpResponse("this is about us")

    # return render(request, 'shop/index.html')

def contact(request):
    return HttpResponse("this is contact")

    # return render(request, 'shop/index.html')

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


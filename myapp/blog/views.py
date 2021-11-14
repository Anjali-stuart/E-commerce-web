from django.shortcuts import render ,HttpResponse, redirect
from .form import EmpForm,StudentForm,StuForm
# Create your views here.
def index(request):
    # Emp = EmpForm()
    # Stu = StuForm()
    # form  = StudentForm()
    if request.method=="POST":
        form = EmpForm(request.POST)
        if form.is_valid():
            try:
                return  redirect(' /')
            except:
                pass
        else:
            form = EmpForm()
        return render(request,'blog/index.html', {'form':form})

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


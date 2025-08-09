from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,"myapp/index.html")

def About_page(request):
    return render(request,"myapp/About.html")

def Contact_Page(request):
    return render(request,"myapp/Contact.html")

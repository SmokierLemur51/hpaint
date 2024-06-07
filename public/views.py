from django.shortcuts import render

# Create your views here.

def index(request):
    context = {}
    return render(request, "public/index.html", context)



def services(request):
    context = {}
    return render(request, "public/services.html", context)
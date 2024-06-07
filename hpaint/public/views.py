from django.shortcuts import render


def index(request):
    context = {"title": "Higginbotham Painting"}
    return render(request, "public/index.html", context)


# our story
def about(request):
    context = {"title": "Our Story"}
    return render(request, "public/about.html", context)


def services(request):
    context = {"title": "Services"}
    return render(request, "public/services.html", context)


def contact(request):
    context = {"title": "Contact Us"}
    return render(request, "public/contact.html", context)



def residential(request):
    context = {"title": "Residential Services"}
    return render(request, "public/residential.html", context)



def commercial(request):
    context = {"title": "Commercial Services"}
    return render(request, "public/commercial.html", context)



def exterior(request):
    context = {"title": "Exterior Services"}
    return render(request, "public/exterior.html", context)


def testimonials(request):
    context = {"title": "Testimonials"}
    return render(request, "public/testimonials.html", context)


"""Post forms"""
def new_contact(request):
        
    return HttpResponse(reverse())
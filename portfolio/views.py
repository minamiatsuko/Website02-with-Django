from django.shortcuts import render,HttpResponse
from portfolio.models import Contact

# Create your views here.
def home(request):
    context = {"name": 'Nan', 'from':'Django'}
    return render(request, 'home.html', context)

def about(request):
     context = {"name": 'Nan', 'from':'Django'}
    # return HttpResponse("This is my about (/about)")
     return render(request, 'about.html', context)

def skills(request):
     context = {"name": 'Nan', 'from':'Django'}
    # return HttpResponse("This is my about (/about)")
     return render(request, 'skills.html', context)

def projects(request):
    context = {"name": 'Nan', 'from':'Django'}
    # return HttpResponse("This is my project (/project)")
    return render(request, 'projects.html', context)

def anime(request):
    context = {"name": 'Nan', 'from':'Django'}
    # return HttpResponse("This is my project (/project)")
    return render(request, 'anime.html', context)

def contact(request):
    if request.method=="POST":
        name = request.POST['name']
        email = request.POST['email']
        desc = request.POST['desc']
        print(name, email, desc)
        ins = Contact(name=name, email=email, desc=desc)
        ins.save()
        print("The data has been written to the db")

    context = {"name": 'Nan', 'from':'Django'}
    # return HttpResponse("This is my contact (/contact)")
    return render(request, 'contact.html', context)



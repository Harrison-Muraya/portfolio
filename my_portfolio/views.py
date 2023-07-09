from django.shortcuts import render
from django.http import HttpResponse
from . form import UserForm

def index(request):

    return render(request, 'my_portfolio/home.html')


def register(request):
    form = UserForm()
    if request.method =='POST':
        #print(request.POST)
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request, 'my_portfolio/register.html', {'form':form})

def profile(request):
    return render(request, 'my_portfolio/profile.html')

def education(request):

    return render(request,'my_portfolio/education.html')

def profession(request):

    return render(request,'my_portfolio/profession.html')

def skills(request):

    return render(request,'my_portfolio/skills.html')
def experience(request):

    return render(request,'my_portfolio/experience.html')

from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Course
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse

# Create your views here.
def homePage(request):
    return render(request,'onlineUniversity/home.html')


def coursePage(request):
    Course_list=Course.objects.all()
    return render(request,'onlineUniversity/courses.html', context={'course':Course_list})

def userLogin(request):
    return render(request,'onlineUniversity/userLogin.html')

def userRegistration(request):
    return render(request,'onlineUniversity/userRegistration.html')

def userLogedin(request):
    username=request.POST.get('username')
    password=request.POST.get('password')

    user=authenticate(request=request,username=username,password=password)

    if user is not None:
        login(request=request,user=user)
        return HttpResponseRedirect(reverse("home"))
    else:
        messages.error(request,"Error in login! Invalid Details")
        return HttpResponseRedirect(reverse("login"))




from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("First line .") #Return Text

def greet(request):
    return HttpResponse("Hello Django")

def rec(request):
    return HttpResponse("Welcome")

def xyz(request):
    return HttpResponse("Good bye")
def abc(request):
    return HttpResponse("Server is ready now")
def de(request):
    return HttpResponse("Just type word")
def fg(request):
    return HttpResponse("String ")
def hij(request):
    return HttpResponse("path ")

def home(request):
    return render(request, 'Part_1/index.html') #Return html file


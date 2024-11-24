from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "hello/index.html") #here it renders a whole file

def brian(request):
    return HttpResponse("HELLO, RACHEL")  #each def view is a new page that renders a string

def rachel(request):
    return HttpResponse("Whatssup??") 

def greet(request, name):
   # return HttpResponse(f"Hello, {name.capitalize()}!")
   return render (request, "hello/greet.html", {
       "name": name.capitalize()
   })
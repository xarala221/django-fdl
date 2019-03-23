from django.shortcuts import render
from django.http import HttpResponse

def index(request):
  if request.user.is_authenticated:
    message = "Hello User"
  else:
    message = "Hello FDL"
  return render(request, "blog/index.html", {'message': message})

def about(request):
  about_me = "Xarala, Developer"
  return render(request, "blog/about.html", {'about_me': about_me})
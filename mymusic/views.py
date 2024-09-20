from django.shortcuts import render

# Create your views here.
def index(request):
  return render(request, "mymusic/index.html")

def addmusic(request):
  pass

def myplaylist(request):
  pass

def musiccalendar(request):
  pass
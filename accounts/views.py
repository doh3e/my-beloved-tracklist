from django.shortcuts import render

# Create your views here.
def join(request):
  return render(request, "accounts/join.html")

def login(request):
  pass

def mypage(request):
  pass
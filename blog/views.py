from django.shortcuts import render

# Create your views here.

def index(reqest): 
    return render(reqest, 'blog/index.html')

def posts(reqest): 
    pass

def post(request):
    pass
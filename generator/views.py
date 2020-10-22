from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request,"generator/templ.html")

def password(request):
    char = list("abcdefghijklmnopqrstuvwxyz")
    
    if request.GET.get('uppercase'):
        char.extend(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
        
    if request.GET.get('Numbers'):
        char.extend(list("1234567890"))
        
    if request.GET.get('Specialcharacters'):
        char.extend(list("!@#$%^&*"))
        
    length = int(request.GET.get('Length'))
    password = ""
    for i in range(length):
        password += random.choice(char)
    print(char)     
    
    return render(request, "generator/password.html",{"password": password})



def about(request):
    return render(request,"generator/about.html")
    


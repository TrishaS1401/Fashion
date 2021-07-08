from django.shortcuts import render, HttpResponse, redirect
from myapp.models import log, contacts
from django.contrib import messages
import re
# Create your views here.

def account(request):
    user=log.objects.all()
    return render(request, 'account.html', {'users' : user,})
def about(request):
    user = log.objects.all()
    return render(request, 'about.html', {'users' : user,})
def cart(request):
    user=log.objects.all()
    return render(request, 'cart.html', {'users' : user,})
def contact(request):
    if request.method == "POST":
        fn = request.POST.get('fn')
        ln = request.POST.get('ln')
        ms = request.POST.get('ms')
        ad = request.POST.get('ad')
        print(fn,ln,ms,ad)
        user1 = contacts(firstname=fn, lastname=ln, message=ms, additionaldetails=ad)
        user1.save()
    user=log.objects.all()
    return render(request, 'contact.html', {'users' : user,})

def index(request):
    user=log.objects.all()
    return render(request, 'index.html', {'users' : user,})
def productDetails(request):
    user=log.objects.all()
    return render(request, 'product-details.html', {'users' : user,})
def products(request):
    user=log.objects.all()
    return render(request, 'products.html', {'users' : user,})

def registration(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        def ispresent(str):
            regex = ("^(?=.*[a-z])(?=." +
            "*[A-Z])(?=.*\\d)" +
            "(?=.*[-+_!@#$%^&*., ?]).+$")
            p = re.compile(regex)
            if(re.search(p, str) and len(str) >= 8):
                return True
            else:
                return False
        a = log.objects.filter(email=email).values('email')
        if a:
            messages.error(request, 'This email already exists!')
            return render(request, 'account.html')
        elif ispresent(password):
            user = log(username=name, email=email, password=password)
            user.save()
        else:
            messages.error(request, 'Password error')
            return render(request, 'account.html')
    return render(request, 'account.html')

def logout(request):
     del request.session['email']
     return redirect("/")

def login(request):
    if request.method == "POST":
        email = request.POST.get('email1')
        password = request.POST.get('password1')
        user=log.objects.all()
        a = log.objects.filter(email=email,password=password).values('email','password')
        print(a)
        if a:
            user1=log.objects.get(email=email)
            request.session['email'] = user1.email
            return render(request, 'index.html', {'users' : user,})
        else:
            messages.error(request, 'Invalid Credentials!')
            return redirect("/reg")
    else:
        return redirect("/login")


import django.db.utils
from django.shortcuts import render
from django.contrib.auth.hashers import make_password, check_password
import traceback
from main.models import User
from django.http import HttpResponse

def login(request):
    if request.session.get("logged_in"):
        return HttpResponse(status=302, headers={"Location": "/product"})
    if request.method == "GET":
        return render(request, 'main/login.html')
    if request.method == "POST":
        username = request.POST.get("login")
        pass_raw = request.POST.get("password")
        try:
            user = User.objects.get(username=username)
            if not check_password(pass_raw, user.password):
                raise User.DoesNotExist
            request.session["logged_in"] = True
            request.session["user_id"] = user.user_id
        except User.DoesNotExist as e:
            return render(request, 'main/login.html', {"error": "Invalid username or password"})
        return HttpResponse(status=302, headers={"Location": "/product"})


def signup(request):
    if request.session.get("logged_in"):
        return HttpResponse(status=302, headers={"Location": "/product"})
    if request.method == "GET":
        return render(request, 'main/signup.html')
    if request.method == "POST":
        username = request.POST.get('login')
        password = make_password(request.POST.get('password'))
        user = None
        try:
            user = User.objects.create(username=username, password=password)
        except django.db.utils.IntegrityError as e:
            return render(request, 'main/signup.html', {"error": "User already exists"})
        except Exception as e:
            return render(request, 'main/signup.html', {"error": "Internal Server Error"})
        request.session["logged_in"] = True
        request.session["user_id"] = user.user_id
        return HttpResponse(status=302, headers={"Location": "/product"})

def product(request):
    return render(request, 'main/product.html')

def logout(request):
    request.session.clear()
    return HttpResponse(status=302, headers={"Location": "/"})
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout

from .models import Product
from .forms import AddUserForm, LoginUserForm


def home(request):
    context = {
        'slider_products': Product.objects.filter(show_slider=True).all(),
        'other_products': Product.objects.filter(show_slider=False).all()
    }
    return render(request, 'home.html', context)



def create_user(request):
    # if request.user.is_authenticated():
    #     redirect("home")
    if request.method == "POST":
        form = AddUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = make_password(form.cleaned_data.get('password1'))
            User.objects.create(username=username, password=password, email='')
            return redirect("home")
    else:
        form = AddUserForm()
    return render(request, "forms/create_user.html", { "form": form })



def login_user(request):
    # if request.user.is_authenticated():
    #     redirect("home")
    error = ""
    if request.method == "POST":
        form = LoginUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            print(user)
            if user:
                login(request, user)
                return redirect("home")
            else:
                error = "نام کاربری یا رمز عبور اشتباه است"
    else:
        form = LoginUserForm()
    return render(request, "forms/login_user.html", { "form": form, "error": error })


def logout_user(request):
    logout(request)
    return redirect("home")



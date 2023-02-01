from django.shortcuts import redirect, render
from login.forms import HandelLoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def login_(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = HandelLoginForm(request.POST, data=request.POST)
            if fm.is_valid():
                user_name = fm.cleaned_data['username']
                user_password = fm.cleaned_data['password']
                user = authenticate(username=user_name, password=user_password)
                if user is not None:
                    login(request, user)
                    return redirect('/')
        else:
            fm = HandelLoginForm()
        return render(request, 'login/login.html', {'form': fm})
    else:
        return redirect("/")


def signup(request):
    if not request.user.is_authenticated:
        username_msg = ""
        email_msg = ""
        if request.method == 'POST':
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            confirm_password = request.POST['confirm_password']
            user_valid_check = User.objects.filter(username=username).exists()
            email_valid_check = User.objects.filter(email=email).exists()
            if user_valid_check:
                username_msg = "User name already exist, please choose new one."
            else:
                user = User.objects.create_user(
                    username=username, password=password, email=email, first_name=first_name, last_name=last_name)
        return render(request, 'login/signup.html', {'umsg': username_msg, 'email_msg': email_msg})
    else:
        return redirect('/login')

# logout


def logout_(request):
    logout(request)
    return redirect('/')

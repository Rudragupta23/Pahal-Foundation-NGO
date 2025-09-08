from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group

# Create your views here.

def index(request):
    return render(request, 'pahal/index.html')

def error_page(request):
    return render(request, 'pahal/error.html')

def register(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, "User Already Exists.")

        user = User.objects.create_user(
            first_name = first_name,
            email = email,
            username = username
        )
        user.set_password(password)
        user.save()

        group = Group.objects.get(name='default')
        user.groups.add(group)

        return redirect('/login/')

    return render(request, 'pahal/signup.html')
def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(request, "Invalid Username")

        user = authenticate(username=username, password=password)
        if user is None:
            messages.error(request, "Incorrect password")
        else:
            login(request, user)
            return redirect("/")

    return render(request, 'pahal/login.html')
def logout_page(request):
    logout(request)
    return redirect('/')

@login_required(login_url="/login")
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('/login')
        else:
            messages.error(request, "Input fields are not valid.")
    return render(request, "pahal/change_password.html")

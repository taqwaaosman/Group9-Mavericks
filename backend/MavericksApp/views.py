from django.http import HttpResponse
from django.shortcuts import render

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def login_view(request):
    print("Logging in...")
    if request.method == 'POST':
        print("POST request received.")
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(f"Username: {username}, Password: {password}")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print("User authenticated.")
            login(request, user)
            print("User logged in.")
            return redirect('home')  # Redirect to your home page after login
        else:
            print("Invalid login attempt.")
            # Handle invalid login
            return render(request, 'index.html', {'error': 'Invalid username or password'})
    print("Rendering login form...")
    return render(request, 'LoginForm.html')


def index(request):
    print("Rendering index page...")
    return render(request, 'index.html')

def home(request):
    print("Rendering home page...")
    return render(request, 'home.html')

# signup page
def registration(request):
    print("Registering new user...")
    if request.method == 'POST':
        print("POST request received.")
        print("POST payload:", request.POST)
        form = UserCreationForm(request.POST)
        if form.is_valid():
            print("Form is valid.")
            user = form.save()
            print("User registered successfully.")
            login(request, user)
            print("User logged in.")
            return redirect('home')  # Redirect to your login page after signup
        else:
            print("Form is not valid.")
            # Pass form object to frontend for display
            return render(request, 'registration.html', {'form': form})
    else:
        print("Rendering registration form...")
        form = UserCreationForm()
    return render(request, 'registration.html', {'form': form})

from django.http import HttpResponse
from django.shortcuts import render

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Expense
from .forms import ExpenseForm
from django.db.models import Sum

 # used chatgbt to create console logs for all events and steps in the code below so that I could debug my code by looking at the console
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


def expense(request):
    print("Expense view function called.")

    if request.method == 'POST':
        print("POST request received.")
        form = ExpenseForm(request.POST)
        if form.is_valid():
            print("Form is valid.")
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            print("Expense saved successfully.")
            return redirect('expense')
        else:
            print("Form is not valid.")
    else:
        print("GET request received.")
        form = ExpenseForm()

    expenses = Expense.objects.filter(user=request.user)
    total_expenses = expenses.aggregate(total=Sum('amount'))['total'] or 0
    print(f"Total expenses: {total_expenses}")

    print("Rendering expense.html template.")
    return render(request, 'expense.html', {'form': form, 'expenses': expenses, 'total_expenses': total_expenses})
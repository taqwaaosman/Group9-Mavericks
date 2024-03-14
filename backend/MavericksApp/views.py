from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to your home page after login
        else:
            # Handle invalid login
            return render(request, 'LoginForm.html', {'error': 'Invalid username or password'})
    return render(request, 'LoginForm.html')
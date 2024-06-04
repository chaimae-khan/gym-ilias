from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User



def home(request):
  return redirct('/home/')

def table(request):
   return render(request, "authenticate/index.html")

def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        
        if not User.objects.filter(username=username).exists():  # Fixed the typo and indentation
            messages.error(request, "Invalid username")
            return redirect('/login_user')
        
        if user is None:  # Corrected the logic for invalid password
            messages.error(request, "Invalid password")
            return redirect('/login_user')
        else:
            login(request, user)  # Corrected the order of arguments for login
            return redirect("/home")
    
    return render(request, "authenticate/login.html")

def register_page(request):
    # Check if the HTTP request method is POST (form submission)
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
         
        # Check if a user with the provided username already exists
        user = User.objects.filter(username=username)
         
        if user.exists():
            # Display an information message if the username is taken
            messages.info(request, "Username already taken!")
            return redirect('/register/')
         
        # Create a new User object with the provided information
        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username
        )
         
        # Set the user's password and save the user object
        user.set_password(password)
        user.save()
         
        # Display an information message indicating successful account creation
        messages.info(request, "Account created Successfully!")
        return redirect('/register/')
     
    # Render the registration page template (GET request)
    return render(request, 'authenticate/regester.html')

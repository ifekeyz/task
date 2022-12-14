from django.shortcuts import render,redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User

# Create your views here.
def register(request):
    if request.method == 'POST':
        # Get from values
        first_name = request.POST['first']
        last_name = request.POST['last']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # check if passwords match
        if password == password2:
           
            # check Username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'That username is taken')
                
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'That email is been used')
                   
                else:
                    # return new auth
                    user = User.objects.create_user(username=username, password=password, email=email,
                    first_name=first_name, last_name=last_name)
                    user.save()
                    return f"{user} successfully registered"
                   
        else:
            messages.error(request, 'passwords do not match')
            # return redirect('')
    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        # Login User
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'you are now logged in')
            return user

        else:
            messages.error(request, 'Invalid credentials')
            # return redirect('login')
    return render(request, '')

def deposite(request):
    return

def withdraw(request):
    return

def balance(request):
    return

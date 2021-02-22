from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.


def welcome(request):
    return render(request, 'index.html')


def login(request):
    if request.method == 'POST':
        # fetch the data
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None: 
            # then login access to user(auth is use for verify)
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'invalid credentials')
    else:
        return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        # fetching field value which is entered by user in the field(we get the user data)
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        Password1 = request.POST['password1']
        password2 = request.POST['password2']

        if Password1 == password2:  # validation
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email taken")
                return redirect('register')
            else:
                # create user object
                user = User.objects.create_user(
                    username=username, password=Password1, email=email, first_name=first_name, last_name=last_name)
                user.save()  # save data into database
                
                return redirect('login')
        else:
            messages.info(request, "password not matching..")
            return redirect('register')
        return redirect('/')

    else:
        return render(request, 'register.html')

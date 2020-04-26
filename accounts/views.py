from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User

# Create your views here.
def register(request):
    if request.method == 'POST':

        #Get form values
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']

        if password == password2:
            #check username 
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username is taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email is taken')
                    return redirect('register') 
                else: 
                    #create the user- push to database
                    user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                    #direct login after register
                        # auth.login(request, user)
                        # messages.success(request, 'you are now logged in')
                        # return redirect('index')
                    #redirect to login page
                    user.save()
                    messages.success(request, 'you can now log in')
                    return redirect('login')

        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')

    else:
        return render(request, 'accounts/register.html')

    

def login(request):
    return render(request, 'accounts/login.html')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')

def logout(request):
    return redirect('index')



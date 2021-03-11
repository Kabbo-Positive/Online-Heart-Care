from django.shortcuts import HttpResponse, get_object_or_404, redirect, render
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Create your views here.

from . models import Nurse




def home(request):
    nurse = Nurse.objects.all()

    

    return render(request, 'home.html', {'nurse':nurse,} )


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Enter a valid username & password')
            return redirect('login')

    else:
        return render(request, 'login.html')
        

    



# Registration View
def registration(request):
    
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username taken ')
                return redirect (request, 'registration')

            elif User.objects.filter(email=email).exists():
                messages.info(request,'email taken')
                return redirect ('registration')
                

            else:
                user= User.objects.create_user(username= username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                
                messages.info(request, 'enter username & password')
                return redirect ('login')
                

        else:
            messages.info(request, 'password not matching')
            return redirect ('registration')
        


    else:
        return render(request,'registration.html')
        


def logout(request):
    auth.logout(request)
    return redirect('/')
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.
def logout(request):
    auth.logout(request)
    return redirect('/')



def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'login yoki parol xato')
            return redirect('login')
    else:
        return render(request, 'login.html')

        


def reg(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        
        if password1==password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'email olingan')
                return render(request, 'reg.html')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'login olingan')
                return render(request, 'reg.html')
            else:
                user=User.objects.create_user(username=username, email=email, first_name=first_name, last_name=last_name, password=password1)
                user.save()
        else:
            messages.info(request, 'parol bir xil emas')
            return render(request, 'reg.html')
        return redirect('/')
    else:
        return render(request, 'reg.html')


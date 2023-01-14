from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    return render(request, 'users/user.html')

def login_view(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request, username=username, password=password)
        userItem=User.objects.all()
        if user is not None:
            login (request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
           
            return render(request, 'users/login.html',{
                'message':'You not auhtenticate.',
                'us':userItem
            })
                
        
    return render(request, 'users/login.html')

def logout_view(request):
    logout(request)
    return render(request, 'users/login.html',{
        'message':'Logged out.'
    })
def register_user(request):
    if request.method=='POST':
        registerForm=UserCreationForm(request.POST)
        if registerForm.is_valid():
            registerForm.save()
            username=registerForm.cleaned_data['username']
            password=registerForm.cleaned_data['password1']
            user=authenticate(username=username,password=password)
            login (request,user)
           
            return redirect('beginen')
    else:
         registerForm=UserCreationForm()
    return render(request, 'users/register.html', {
        'myRegister':registerForm
    })
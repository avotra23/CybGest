from django.shortcuts import render, HttpResponse, redirect
from .forms import LoginForm, SignupForm
from django.contrib.auth import get_user_model, login as auth_login, logout as auth_logout

# Create your views here.

def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            User = get_user_model()
            user = User.objects.get(email=email)
            if user is not None and user.check_password(password):
                return HttpResponse(f"Bonjour{user.username}")
    else :
        form = LoginForm()
    return render(request, 'login.html', {'form':form})

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request,user)
            return HttpResponse("Ajout succes")
    else:
        form = SignupForm()
    return render(request,'signup.html',{'form':form})

def logout(request):
    auth_logout(request)
    return redirect('login')

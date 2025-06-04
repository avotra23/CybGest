from django.shortcuts import render, HttpResponse, redirect
from .forms import LoginForm, SignupForm, PostForms
from django.contrib.auth import get_user_model, login as auth_login, logout as auth_logout
from .models import Poste
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
# Create your views here.

@csrf_exempt
@require_POST
def demande(request):
    ip = request.POST.get('ip')
    action = request.POST.get('action')
    try :
        poste = Poste.objects.get(ip=ip)
    except Exception as e:
        print("Erreur",e)
    if action =="autoriser":
        poste.etat = "autoriser"
    elif action == "refuser":
        poste.etat = "refuser"
    else:
        return JsonResponse({'success':False,'error':'action invalid'})
    poste.save()
    return JsonResponse({'success':True,'etat':poste.etat})
def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            User = get_user_model()
            user = User.objects.get(email=email)
            if user is not None and user.check_password(password):
                auth_login(request,user)
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

def cybges(request):
    postes = Poste.objects.all()
    if request.user.is_authenticated:
        user_info = {
            'username': request.user.username,
            'email': request.user.email,
        }
    if request.method == "POST" :
        form = PostForms(request.POST)
        if form.is_valid():
            form.save()
    form = PostForms()
    return render(request,'cyb.html',{'user':user_info,'form':form,'poste':postes})

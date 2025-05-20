from django.shortcuts import render
from .forms import LoginForm
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

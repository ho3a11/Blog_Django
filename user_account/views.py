from django.shortcuts import render ,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . forms import UserRegistrationForm,LoginForm
# from django.contrib.auth import  authenticate, login, logout, update_session_auth_hash  
from django.contrib.auth import login, authenticate,logout

def singup(request):
    
    # if request.method == 'POST':
    #     form = UserCreationForm(request.POST)
    #     if form.is_valid():
    #         form.save()
            
    #         return redirect('article:show_article')
    # else:
    #     form = UserCreationForm()

    # return render (request, 'singup.html', {'form':form})
    
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if cd['password'] == cd['repassword']:
                user = User.objects.create_user(cd['username'], cd['email'], cd['password'])
                user.first_name = cd['first_name']
                user.last_name = cd['last_name']
                user.save()
                login(request,user)
                return redirect('blog:index')
    else:
        form = UserRegistrationForm()
    return render(request, 'singup.html', {'form': form})



def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                return redirect('blog:index')
            else:
                return redirect('login.html')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('user_account:login')
    
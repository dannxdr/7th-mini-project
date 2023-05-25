from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth import login, authenticate
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from .models import User_info

def signup(request):
    res_data={}
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        re_password = request.POST['re_password']
        
        if not (username and password and re_password):
            res_data['error'] = '모든 값을 입력해야 합니다.'
        if password != re_password:
            res_data['error'] = '비밀번호가 다릅니다.'
        else:
            user = User_info(username=username, password=make_password(password))
            user.save()
            user = User.objects.create_user(
                username=username,
                password = password,
            )
            auth.login(request,user)
            return redirect('/')
        res_data['active'] = "signup"
    return render(request, 'signup/signup.html', res_data)

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            return render(request, 'login/login.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'login/login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
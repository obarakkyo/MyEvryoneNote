from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db import IntegrityError 
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib import messages

# Create your views here.
def userlogapp_base(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        # print(username, password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            mnnvoice_url = reverse('userlogapp:search')
            return redirect(mnnvoice_url)
        else:
            messages.error(request, 'ログインに失敗しました。')
            return render(request, 'userlogapp/login.html', {'errormassage':'ログインに失敗しました。再度ログインしてください。'})
    return render(request, 'userlogapp/login.html', {})

def SearchFunction(request):
    return render(request, 'userlogapp/search.html', context={})

def signupfunc(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password_again = request.POST['passwordagain']

        if password != password_again:
            messages.error(request, '再入力パスワードが違います！')
            return render(request, 'userlogapp/signup.html', {'errormassage':'再入力パスワードが違います！'})
        print(password_again)
        try:
            user = User.objects.create_user(username, '', password)
            return redirect('userlogapp:login')
        except IntegrityError:
            messages.error(request, 'そのusernameは既に存在しています。')
            return render(request, 'userlogapp/signup.html', {'errormassage':'そのusernameは既に存在しています。'})
    return render(request, 'userlogapp/signup.html', {})

def logoutfunc(request):
    print(request.user.username, 'をログアウトします')
    logout(request)
    return redirect('userlogapp:login')

def base_func(request):
    return render(request, 'base.html', context={})
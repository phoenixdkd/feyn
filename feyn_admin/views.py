
# coding=utf-8
# Create your views here.

from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


def index(request):
    user = auth.authenticate(username='john', password= '123456')
    if user is not None:
        data = {'databases': ['mysql', 'asm'], 'loginStatus':True}
    else:
        data = {'databases': ['mysql', 'asm'], 'loginStatus':False}
    return render(request, 'index.html', {'data': data})


def login_view(request):
    if 'next' in request.GET:
        redirect_to = request.GET['next']
    else:
        redirect_to = '/'
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(redirect_to)
    return render(request, 'login.html', locals())


def logout_view(request):
    logout(request)
    print request.META
    redirect_to = request.META['HTTP_REFERER']
    return HttpResponseRedirect(redirect_to)


def user_add(request):
    if 'next' in request.GET:
        redirect_to = request.GET['next']
    else:
        redirect_to = '/'
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(username=username, password=password, email='')
        user.save()
    user = authenticate(username=username, password=password)
    login(request, user)
    return HttpResponseRedirect(redirect_to)


    return render(request, 'user_add.html', {'user': username, 'password': password})


def user_info(request):
    return render(request, 'user_info.html')

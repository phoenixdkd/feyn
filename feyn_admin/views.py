
# coding=utf-8
# Create your views here.

from django.shortcuts import render,redirect
from django.http import HttpResponse
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
    data = {'databases': ['mysql', 'asm']}
    return render(request, 'login.html', {'data': data})


def logout_view(request):
    data = {'databases': ['mysql', 'asm']}
    logout(request)
    return render(request, 'login.html', {'data': data})


def user_add(request):
    username = request.GET['user']
    password = request.GET['password']

    return render(request, 'user_add.html', {'user': username, 'password': password})

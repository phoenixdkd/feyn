
# coding=utf-8
# Create your views here.
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.contrib import auth
from django.contrib.auth.models import User


def index(request):
    user = auth.authenticate(username='john', password= '123456')
    if user is not None:
        data = {'databases': ['mysql', 'asm'], 'loginStatus':True}
    else:
        data = {'databases': ['mysql', 'asm'], 'loginStatus':False}
    return render(request, 'index.html', {'data': data})


def login(request):
    data = {'databases': ['mysql', 'asm']}
    return render(request, 'login.html', {'data': data})


def user_add(request):
    username = request.GET['user']
    password = request.GET['password']
    request.session['member_id'] = username
    return render(request, 'user_add.html', {'user': username, 'password': password})


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


def cmb_list_report(request):
    linux_array = []
    template = ['CPU使用率', '内存使用率']
    for i in range(10):
        attrArray = [{'attrName': 'CPU使用率', 'top': i+1, 'avg': i + 0.5},
                     {'attrName': '内存使用率', 'top': i+2, 'avg': i + 1.5}]
        item = {'name': 'host'+str(i), 'ip': '192.168.0.'+str(i),
                'type': i <= 5 and '物理机' or '虚拟机', 'attrArray':attrArray}
        linux_array.append(item)

    win_array = []
    template = ['CPU使用率', '内存使用率']
    for i in range(10):
        attrArray = [{'attrName': 'CPU使用率', 'top': i+3, 'avg': i + 2.5},
                     {'attrName': '内存使用率', 'top': i+4, 'avg': i + 3.5}]
        item = {'name': 'host'+str(i), 'ip': '192.168.0.1'+str(i),
                'type': i <= 5 and '物理机' or '虚拟机', 'attrArray':attrArray}
        win_array.append(item)

    aix_array = []
    template = ['CPU使用率', '内存使用率']
    for i in range(10):
        attrArray = [{'attrName': 'CPU使用率', 'top': i+5, 'avg': i + 4.5},
                     {'attrName': '内存使用率', 'top': i+6, 'avg': i + 5.5}]
        item = {'name': 'host'+str(i), 'ip': '192.168.0.2'+str(i),
                'type': i <= 5 and '物理机' or '虚拟机', 'attrArray':attrArray}
        aix_array.append(item)
    data = {'linux_array': linux_array,
            'win_array': win_array,
            'aix_array': aix_array,
            'template': template}
    return render(request, 'cmb_list_report.html', data)


def cmb_capability_report(request):
    array = []
    template = ['CPU使用率', '内存使用率']
    for i in range(10):
        attrArray = [{'attrName': 'CPU使用率', 'top': i, 'avg': i - 0.5},
                     {'attrName': '内存使用率', 'top': i+1, 'avg': i + 0.5}]
        item = {'name': 'host'+str(i), 'ip': '192.168.0.'+str(i),
                'type': i <= 5 and '物理机' or '虚拟机', 'attrArray':attrArray}
        array.append(item)
    return render(request, 'cmb_capability_report.html', {'array': array, 'template': template})

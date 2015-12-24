# coding=utf-8

from django.shortcuts import render

# Create your views here.


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
    return render(request, 'cmb_demo/cmb_list_report.html', data)


def cmb_capability_report(request):
    array = []
    template = ['CPU使用率', '内存使用率']
    for i in range(10):
        attrArray = [{'attrName': 'CPU使用率', 'top': i, 'avg': i - 0.5},
                     {'attrName': '内存使用率', 'top': i+1, 'avg': i + 0.5}]
        item = {'name': 'host'+str(i), 'ip': '192.168.0.'+str(i),
                'type': i <= 5 and '物理机' or '虚拟机', 'attrArray':attrArray}
        array.append(item)
    return render(request, 'cmb_demo/cmb_capability_report.html', {'array': array, 'template': template})
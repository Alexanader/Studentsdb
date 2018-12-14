# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse

# Views for Students
def students_list(request):
    students = (
        {'id': 1,
         'first_name': u'Andriy',
         'last_name': u'Korost',
         'ticket': 123,
         'image': 'img/podoba3.jpg'},

        {'id':2,
         'first_name': u'Vitaliy',
         'last_name': u'Podoba',
         'ticket': 254,
         'image': 'img/me.jpeg'},

        {'id':3,
         'first_name': u'Taras',
         'last_name': u'Pritula',
         'ticket': 5332,
         'image': 'img/piv.png'}
    )
    return render(request,'students/students_list.html', {'students': students})
def students_edit(request, sid):
    return HttpResponse('<h1>Edit Student %s</h1>' % sid)
def students_add(request,):
    return HttpResponse('<h1>Add Student %s</h1>')
def students_delete(request, sid):
    return HttpResponse('<h1>Delete Student %s</h1>' % sid)

# Views for Group
def groups_list(request):
    groups = (
        {'id': 1,
        'name': u'MtM-21',
        'captain': u'Yachmenov Oleg'
        },

        {'id': 2,
        'name': u'MtM-22',
        'captain': u'Vitaliy Podoba'
        },

        {'id': 3,
        'name': u'MtM-23',
        'captain': u'Ivanov Andriy'}
    )
    return render(request,'groups/groups_list.html',{'groups': groups})
def groups_edit(request, gid):
    return HttpResponse('<h1>Edit Group %s</h1>' % gid)
def groups_add(request):
    return HttpResponse('<h1>Add Group %s</h1>')
def groups_delete(request, gid):
    return HttpResponse('<h1>Delete Group %s</h1>' % gid)
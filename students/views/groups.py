# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse

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
    return render(request,'students/group.html',{'groups': groups})
def groups_edit(request, gid):
    return HttpResponse('<h1>Edit Group %s</h1>' % gid)
def groups_add(request):
    return HttpResponse('<h1>Add Group %s</h1>')
def groups_delete(request, gid):
    return HttpResponse('<h1>Delete Group %s</h1>' % gid)
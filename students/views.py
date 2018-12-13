from django.shortcuts import render
from django.http import HttpResponse

# Views for Group
def students_list(request):
    return render(request,'students/students_list.html', {})
def students_edit(request, sid):
    return HttpResponse('<h1>Edit Student %s</h1>' % sid)
def students_add(request,):
    return HttpResponse('<h1>Add Student %s</h1>')
def students_delete(request, sid):
    return HttpResponse('<h1>Delete Student %s</h1>' % sid)

# Views for Group
def groups_list(request):
    return render(request,'<h1>Groups Listing</h1>')
def groups_edit(request, gid):
    return HttpResponse('<h1>Edit Group %s</h1>' % gid)
def groups_add(request):
    return HttpResponse('<h1>Add Group %s</h1>')
def groups_delete(request, gid):
    return HttpResponse('<h1>Delete Group %s</h1>' % gid)
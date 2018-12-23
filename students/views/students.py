# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from ..models import Student
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Views for Students
def students_list(request):
    students = Student.objects.all()

    #try to order student list
    order_by = request.GET.get('order_by', '')
    if order_by in ('last_name', 'first_name', 'ticket'):
        students = students.order_by(order_by)
        if request.GET.get('reverse','') == '1':
            students = students.reverse()
    #PAGINATE STUDENTS
    paginator = Paginator(students,3)
    page = request.GET.get('page')
    try:
        students = paginator.page(page)
    except PageNotAnInteger:
        #IF PAGE IS NOT AN INTEGER, DELIVER 1ST PAGE.
        students = paginator.page(1)
    except EmptyPage:
        #IF PAGE IS OUT OF RANGE( E. G. 9999), DELIVER
        #LAST PAGE OF RESULTS.
        students = paginator.page(paginator.num_pages)


    return render(request,'students/students_list.html', {'students': students})
def students_edit(request, sid):
    return HttpResponse('<h1>Edit Student %s</h1>' % sid)
def students_add(request,):
    return HttpResponse('<h1>Add Student %s</h1>')
def students_delete(request, sid):
    return HttpResponse('<h1>Delete Student %s</h1>' % sid)
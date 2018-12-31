# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import datetime

from ..models import Student,Group



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
def students_add(request):
    #was form posted?
    if request.method == "POST":
        #was form add button clicked?
        if request.POST.get('add_button') is not None:
            #errors colletion
            errors = {}
            #validate student data will go here
            data = {'middle_name':request.POST.get('middle_name'),
                    'notes':request.POST.get('notes')}

            #validate user input
            first_name = request.POST.get('first_name','').strip()
            if not first_name:
                errors['first_name'] = u"Name is necessary"
            else:
                data['first_name'] = first_name

            last_name = request.POST.get('last_name', '').strip()
            if not last_name:
                errors['last_name'] = u"Last Name is necessary"
            else:
                data['last_name'] = last_name

            birthday = request.POST.get('birthday','').strip()
            if not birthday:
                errors['birthday'] = u"Birthday date is necessary"
            else:
                try:
                    datetime.strptime(birthday, '%Y-%m-%d')
                except Exception:
                    errors['birthday'] = u"Input correct format of data ( exp. 1984-12-30)"
                else:
                    data['birthday'] = birthday

            ticket = request.POST.get('ticket','').strip()
            if not ticket:
                errors['ticket'] = u"Number of ticket is necessary"
            else:
                data['ticket'] = ticket

            student_group = request.POST.get('student_group','').strip()
            if not student_group:
                errors['student_group'] = u"Select student group!"
            else:
                groups = Group.objects.filter(pk=student_group)
                if len(groups) != 1:
                    errors['student_group'] = u"Select direct group"
                else:
                    data['student_group'] = groups[0]


            photo = request.FILES.get('photo')
            if photo:
                data['photo'] = photo

            #save student
            if not errors:
                #create student object
                student = Student(**data)
                #save it to database
                student.save()

                #redirect user to students list
                return HttpResponseRedirect(u'%s?status_message = Student added successufully'% reverse('home'))

            else:
                #render form with errors and previous user input
                return render(request,'students/students_add.html',
                    {'groups':Group.objects.all().order_by('title'),
                     'errors':errors})
        elif request.POST.get('cancel_button') is not None:
            #redirect to home page on cancel button
            return HttpResponseRedirect(
                u'%s?status_massage = Cancellation' % reverse('home'))
    else:
        #initial from render
        return  render(request, 'students/students_add.html',
                       {'groups':Group.objects.all().order_by('title')})


def students_delete(request, sid):
    return HttpResponse('<h1>Delete Student %s</h1>' % sid)
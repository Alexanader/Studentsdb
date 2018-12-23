# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db import models
# Create your models here.
class Student(models.Model):
    """Student Model"""
    class Meta(object):
        verbose_name = u"Student"
        verbose_name_plural = u"Students"

    first_name = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"Name"
    )

    last_name = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"Last_name"
    )

    middle_name = models.CharField(
        max_length=256,
        blank=True,
        verbose_name=u"По-батькові",
        default =''
    )

    birthday = models.DateField(
        blank=False,
        verbose_name=u"Дата народження",
        null = True
    )

    student_gruop = models.ForeignKey('Group',
        verbose_name=u"Група",
        blank=False,
        null=True,
        on_delete=models.PROTECT
    )


    photo = models.ImageField(
        blank=True,
        verbose_name=u"Фото",
        null = True
    )

    ticket = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"Білет"
    )

    notes = models.TextField(
        blank=True,
        verbose_name=u"Додаткові нотатки",
        default='SOME STRING'
    )

    def __unicode__(self):
        return u"%s %s" % (self.first_name, self.last_name)


class Group(models.Model):
    """Group Model"""


    class Meta(object):
            verbose_name = u"Група"
            verbose_name_plural = u"Групи"

    title = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"Назва",
        default='Defoult title')

    student_group = models.ForeignKey('Group',
            verbose_name=u"Група",
            blank = False,
            null = True,
            on_delete=models.PROTECT
            )

    leader = models.OneToOneField('Student',
        verbose_name=u"Староста",
        blank=True,
        null=True,
        on_delete=models.SET_NULL)

    notes = models.TextField(
        blank=True,
        verbose_name=u"Додаткові нотатки",
        default='SOME STRING')


    def __unicode__(self):
        if self.leader:
            return u"%s (%s %s)" % (self.title, self.leader.first_name, self.leader.last_name)

        else:
            return u"%s" % (self.title,)
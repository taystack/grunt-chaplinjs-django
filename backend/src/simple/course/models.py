# from tastypie.utils.timezone import now
from __future__ import (division, print_function, unicode_literals,
                        absolute_import)
from django.contrib.auth.models import User
from django.db import models
from django.db.models import signals, Q
from django.dispatch import receiver
from django.template.defaultfilters import slugify
from simple.models import Clock


class Course(Clock):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):

        return super(Course, self).save(*args, **kwargs)

class Hole(Clock):
    course = models.ForeignKey(Course)
    hole_number = models.IntegerField()
    description = models.CharField(max_length=1024, null=True, blank=True)

    class Meta:
        ordering = ['hole_number']

    def __unicode__(self):
        return "{},{}".format(self.course, self.hole_number)

    def save(self, *args, **kwargs):
        return super(Hole, self).save(*args, **kwargs)
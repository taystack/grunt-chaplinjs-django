from __future__ import print_function, unicode_literals, division
from __future__ import absolute_import
from django.db import models
from django.contrib.contenttypes.models import ContentType

class Clock(models.Model):

    class Meta:
        abstract = True

    created = models.DateTimeField(auto_now_add=True, editable=False)

    updated = models.DateTimeField(auto_now_add=True, editable=False)
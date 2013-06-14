import armet
from django.contrib.auth.models import User
from django.contrib import admin
from armet import resources
from tastypie import fields
# from tastypie.resources import ModelResource
from simple import api
from . import models


class User(admin.ModelAdmin):

    model = models.User

    list_allowed_operations = (
        'create',
        'read',
        'update',
        'destroy',)

    detail_allowed_operations = (
        'create',
        'read',
        'update',
        'destroy',)


class Course(api.ModelResource):

    model = models.Course

    list_allowed_operations = (
        'create',
        'read',
        'update',
        'destroy',)

    detail_allowed_operations = (
        'create',
        'read',
        'update',
        'destroy',)


class Hole(api.ModelResource):

    model = models.Hole

    list_allowed_operations = (
        'create',
        'read',
        'update',
        'destroy',)

    detail_allowed_operations = (
        'create',
        'read',
        'update',
        'destroy',)

from django.contrib.auth.models import User
from tastypie import fields
from tastypie.resources import ModelResource
from course.models import Course, Hole


class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        fields = ['username', 'first_name', 'last_name', 'last_login',
          'email', 'is_superuser', 'is_admin', 'is_active']


class CourseResource(ModelResource):
    user = fields.ForeignKey(UserResource, 'user')

    class Meta:
        model = Course
        queryset = Course.objects.all()
        resource_name = 'course'

class HoleResource(ModelResource):
    course = fields.ForeignKey(CourseResource, 'course')

    class Meta:
        model = Hole
        queryset = Hole.objects.all()
        resource_name = 'hole'
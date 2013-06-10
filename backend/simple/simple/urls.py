# from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import *
from course.api import CourseResource, UserResource, HoleResource
from django.contrib import admin
from tastypie.api import Api

admin.autodiscover()

v1_api = Api(api_name='v1')
v1_api.register(CourseResource())
v1_api.register(HoleResource())
User_api = Api(api_name='users')
User_api.register(UserResource())

urlpatterns = patterns('',
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
    (r'^api/', include(v1_api.urls)),
    (r'^api/', include(User_api.urls)),
)

# from django.conf.urls import patterns, include, url
from __future__ import print_function, unicode_literals
from __future__ import absolute_import, division
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from simple.course import api as course

# Djangos admin module
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
)

# Armet exposing urls
urlpatterns += patterns(
  '',
  url(r'^api/course/', include(course.Course.urls)),
  url(r'^api/course/', include(course.Hole.urls)),
  )

# Static files URL patterns
urlpatterns += staticfiles_urlpatterns()

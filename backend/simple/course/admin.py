from django.contrib import admin
from course.models import Course, Hole

class HoleInline(admin.StackedInline):
    model = Hole
    extra = 1

class CourseAdmin(admin.ModelAdmin):
    model = Course

    inlines = [HoleInline]


admin.site.register(Course, CourseAdmin)
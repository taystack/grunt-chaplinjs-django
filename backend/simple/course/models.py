from tastypie.utils.timezone import now
from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify


class Course(models.Model):
    user = models.ForeignKey(User)
    play_date = models.DateTimeField(default=now, null=True)
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    address = models.CharField(max_length=200, null=True, blank=True)

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        # For automatic slug generation.
        if not self.slug:
            self.slug = slugify(self.name)[:50]

        return super(Course, self).save(*args, **kwargs)

class Hole(models.Model):
    course = models.ForeignKey(Course)
    hole_number = models.IntegerField()
    description = models.CharField(max_length=1024, null=True, blank=True)

    def __unicode__(self):
        return "{},{}".format(self.course, self.hole_number)

    def save(self, *args, **kwargs):
        return super(Hole, self).save(*args, **kwargs)
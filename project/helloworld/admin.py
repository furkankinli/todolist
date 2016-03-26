from django.contrib import admin

# Register your models here.

from helloworld.models import Job, Priority

admin.site.register(Job)
admin.site.register(Priority)

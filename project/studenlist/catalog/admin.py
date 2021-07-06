from django.contrib import admin
from .models import Student, Profile,Comment,Department,University,Faculty

admin.site.register(Student)
admin.site.register(Profile)
admin.site.register(Comment)
admin.site.register(Department)
admin.site.register(University)
admin.site.register(Faculty)
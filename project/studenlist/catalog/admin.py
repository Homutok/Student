from django.contrib import admin
from .models import Student, Profile,Comment,Department

admin.site.register(Student)
admin.site.register(Profile)
admin.site.register(Comment)
admin.site.register(Department)
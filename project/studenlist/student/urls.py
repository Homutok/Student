from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^students/$', views.StudentListView.as_view(), name='student'),
    re_path(r'^student/(?P<pk>\d+)$', views.StudentDetailView.as_view(), name='student_detail'),
    re_path(r'^student/create/$', views.StudentCreate.as_view(), name='student_create'),
    re_path(r'^student/(?P<pk>\d+)/update/$', views.StudentUpdate.as_view(), name='student_update'),
    re_path(r'^student/(?P<pk>\d+)/delete/$', views.StudentDelete.as_view(), name='student_delete'),
    re_path(r'^my_list$', views.my_student_list, name='my_student_filter'),
    re_path(r'^all_list$', views.student_list, name='student_filter'),
    re_path(r'^student/(?P<pk>\d+)/comment/$', views.CommentCreate.as_view(), name='comment_create'),
    re_path(r'^student/(?P<pk>\d+)/comment_delete/$', views.CommentDelete.as_view(), name='comment_delete'),
    re_path(r'^student/(?P<pk>\d+)/comment_upd/$', views.CommentUpdate.as_view(), name='comment_update'),
    re_path(r'^faculty_list/(?P<pk>\d+)$', views.faculty_student_list, name='student_faculty'),
    re_path(r'^department_list/(?P<pk>\d+)$', views.department_student_list, name='student_department'),
]
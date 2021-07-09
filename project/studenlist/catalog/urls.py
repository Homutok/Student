from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.indexView.as_view(), name='index'),
    re_path(r'^signup/$', views.signup, name='signup'),
]

from django.urls import re_path
import views

urlpatterns = [
    re_path(r'^departments/$', views.DepartmentListView.as_view(), name='department'),
    re_path(r'^department/(?P<pk>\d+)$', views.DepartmentDetailView.as_view(), name='department-detail'),
    re_path(r'^department/create/$', views.DepartmentCreate.as_view(), name='department_create'),
    re_path(r'^department/(?P<pk>\d+)/update/$', views.DepartmentUpdate.as_view(), name='department_update'),
    re_path(r'^department/(?P<pk>\d+)/delete/$', views.DepartmentDelete.as_view(), name='department_delete'),
]
from django.urls import re_path
import views

urlpatterns = [
    re_path(r'^universities/$', views.UniversityListView.as_view(), name='university'),
    re_path(r'^university/(?P<pk>\d+)$', views.UniversityDetailView.as_view(), name='university-detail'),
    re_path(r'^university/create/$', views.UniversityCreate.as_view(), name='university_create'),
    re_path(r'^university/(?P<pk>\d+)/update/$', views.UniversityUpdate.as_view(), name='university_update'),
    re_path(r'^university/(?P<pk>\d+)/delete/$', views.UniversityDelete.as_view(), name='university_delete'),
]
from django.urls import path, re_path

from . import views

urlpatterns = [
    path('post/add/', views.post_add, name = 'post_add'),
    re_path(r'^post/update/(?P<pk>\d+)/$', views.post_update, name='post_update'),
]

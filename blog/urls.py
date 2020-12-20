from django.urls import path, re_path

from . import views

urlpatterns =[
    path('',views.post_list, name = 'post_list'),
    path('blog/', views.test_redirect, name = 'test_redirect'),
    path('feedback/', views.feedback, name = 'feedback'),
    re_path(r'^post/(?P<pk>\d+)/(?P<post_slug>[\w-]+)/$', views.post_detail, name = 'post_detail'),
    re_path(r'^category/(?P<category_slug>[\w-]+)/$',views.post_by_category, name = 'post_by_category'),
    re_path(r'^tag/(?P<tag_slug>[\w-]+)/$', views.post_by_tag, name = 'post_by_tag'),
    re_path(r'^author/(?P<pk>\d+)/(?P<author_name>[\w-]+)/$', views.post_by_author, name = 'post_by_author'),
]

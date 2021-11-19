from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('panel/galleryposts/edit/<int:pk>',
         views.galleryedit, name='galleryposts_edit'),
    path('panel/galleryposts/delete/<int:pk>',
         views.gallerydelete, name='galleryposts_delete'),
    url(r'^gallery/$', views.index, name='index'),
    url(r'^panel/galleryposts/add/$',
        views.galleryadmin, name='galleryadmin'),
    url(r'^panel/galleryposts/list/$',
        views.gallerylist, name='gallery_list'),

]

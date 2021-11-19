from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^news/(?P<word>.*)/$', views.article_detail, name='article_detail'),
    url(r'^like/(?P<word>.*)/$', views.like, name='like'),
    url(r'^unlike/(?P<word>.*)/$', views.unlike, name='unlike'),
    url(r'^panel/articles/list/$', views.articles_list, name='articles_list'),
    url(r'^panel/articles/add/$', views.articles_add, name='articles_add'),
    url(r'^panel/articles/del/(?P<pk>\d+)/$',
        views.articles_delete, name='articles_delete'),
    url(r'^panel/articles/edit/(?P<pk>\d+)/$',
        views.articles_edit, name='articles_edit'),
    url(r'^all/articles/(?P<word>.*)/$',
        views.articles_all_show, name='articles_all_show'),
    url(r'^articles/all/$', views.all_articles, name='all_articles'),
    url(r'^search/$', views.all_articles_search, name='all_articles_search'),
    #url(r'^search/$', views.all_serviceproviders_search, name='all_serviceproviders_search'),
]

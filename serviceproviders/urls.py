from django.conf.urls import url
from . import views

urlpatterns = [
	# url(r'^news/(?P<word>.*)/$', views.article_detail, name='article_detail'),
	# url(r'^panel/articles/list/$', views.articles_list, name='articles_list'),
	# url(r'^panel/articles/add/$', views.articles_add, name='articles_add'),
	# url(r'^panel/articles/del/(?P<pk>\d+)/$', views.articles_delete, name='articles_delete'),
	# url(r'^panel/articles/edit/(?P<pk>\d+)/$', views.articles_edit, name='articles_edit'),

 # url(r'^news/(?P<word>.*)/$', views.article_detail, name='article_detail'),
	# url(r'^panel/articles/list/$', views.articles_list, name='articles_list'),
	# url(r'^panel/articles/add/$', views.articles_add, name='articles_add'),
	# url(r'^panel/articles/del/(?P<pk>\d+)/$', views.articles_delete, name='articles_delete'),
	# url(r'^panel/articles/edit/(?P<pk>\d+)/$', views.articles_edit, name='articles_edit'),
	url(r'^serviceproviders/$', views.serviceproviders_list, name='serviceproviders_list'),
	url(r'^panel/serviceproviders/list/$', views.serviceproviders_list, name='serviceproviders_list'),
	url(r'^panel/serviceproviders/add/$', views.serviceproviders_add, name='serviceproviders_add'),
	url(r'^serviceproviders/all/$', views.all_serviceproviders, name='all_serviceproviders'),
	url(r'^serviceproviders/all/(?P<word>.*)/$', views.all_serviceproviders, name='all_serviceproviders'),
	url(r'^serviceproviders/search/$', views.all_serviceproviders_search, name='all_serviceproviders_search'),
	url(r'^serviceproviders/all/search/$', views.all_serviceproviders_search, name='all_serviceproviders_search'),
]

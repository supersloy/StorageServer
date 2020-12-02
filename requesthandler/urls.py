from django.conf.urls import url
from requesthandler import views

urlpatterns = [
    url(r'^api/mapmeta$', views.meta_list),
    url(r'^api/mapmeta/pk/(?P<pk>[0-9]+)$', views.meta_by_pk),
    url(r'^api/mapmeta/title/(?P<title>[а-яА-Яa-zA-Z0-9]+)$', views.meta_by_title),
    url(r'^api/mapfile/upload/(?P<filename>[а-яА-Яa-zA-Z0-9.]+)$', views.upload),
    url(r'^api/mapfile/download/(?P<pk>[0-9]+)$', views.download),
    url(r'^api/mapfile/update/pk/(?P<pk>[0-9]+)$', views.update_by_pk),
    url(r'^api/mapfile/update/title/(?P<title>[а-яА-Яa-zA-Z0-9]+)$', views.update_by_title),
]

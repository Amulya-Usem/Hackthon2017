from django.conf.urls import url

from . import views

urlpatterns = [
    # url(r'^testGet/(?P<userid>\d+)/$', views.testGet, name='test2'),
    # url(r'^testGetParams', views.testGetParams, name='testGetParams'),
    url(r'^getData', views.fetchData, name='getData')
]
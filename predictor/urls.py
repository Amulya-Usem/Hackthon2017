from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^testGet/(?P<userid>\d+)/$', views.testGet, name='test2'),
    url(r'^getEachYearData',views.fetchEachYearData, name='getEachYearData'),
    url(r'^getData', views.fetchData, name='getData')
    # url(r'^getEachYearData', views.getEachYearData, name='getEachYearData') 
]
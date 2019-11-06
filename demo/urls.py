from django.conf.urls import url 
from . import views 

app_name = "demo"
urlpatterns = [ 
     url(r'^$', views.Index.as_view(), name='index'),
     url(r'^download/(?P<path>.*)$', views.Download.as_view(), name='download')
]
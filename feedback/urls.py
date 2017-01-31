from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.showBase, name='showBase'),
    url(r'^submit/$', views.formProcess, name='formProcess'),
]
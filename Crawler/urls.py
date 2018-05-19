from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^new_notice/(?P<location>[a-z]+)/$', views.new_notice)
]
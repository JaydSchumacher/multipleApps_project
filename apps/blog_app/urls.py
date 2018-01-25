from django.conf.urls import url
from . import views

def test(request):
    print "Yay!"

urlpatterns = [
    url(r'^$', views.index),
    url(r'^new', views.new),
    url(r'^create', views.index),
    url(r'^\d', views.show),
]
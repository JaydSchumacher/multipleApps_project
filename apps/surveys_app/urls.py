from django.conf.urls import url
from . import views

def test(request):
    print "In the survey"

urlpatterns = [
    url(r'^$', views.index),
    
]
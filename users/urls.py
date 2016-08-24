from django.conf.urls import include, url
from .views import user_objects, user_object

urlpatterns = [
    url(r'^users/(?P<user>\w+)/objects/$', user_objects),
    url(r'^users/(?P<user>\w+)/objects/(?P<object>\d+)/$', user_object),
]


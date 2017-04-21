from django.conf.urls import url
from ticketsystem import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^requestride/$', views.requestRide),
    url(r'^dropoffRide/$', views.dropoffRide),

]
urlpatterns = format_suffix_patterns(urlpatterns)

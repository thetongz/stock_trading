from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from userApp import views

urlpatterns = [
    url(r'^register', views.register)
]

urlpatterns = format_suffix_patterns(urlpatterns)
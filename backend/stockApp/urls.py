from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from stockApp import views

urlpatterns = [
    url(r'^list', views.list),
    url(r'^currentStockData', views.getCurrentStockData),
    url(r'^comparedValue', views.getComparedValue),
    url(r'^stockValue', views.getStockValue),
    url(r'^buy', views.buyStock),
    url(r'^sell', views.sellStock)
]

urlpatterns = format_suffix_patterns(urlpatterns)
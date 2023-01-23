from . import views,api
from django.urls import path
from Website import views

urlpatterns = [
    path('', views.home, name='home'),
    path('data', views.temperature, name='Data'),
    path('charts/', views.EditorChartView.as_view(), name='CH'),
    path('csv/', views.exp_csv, name='exp-csv'),
    path('api/list', api.Dlist, name='TEMPERATUREList'),
    path('api/post', api.Temperatureviews.as_view(), name='TEMPERATURE_post'),

]

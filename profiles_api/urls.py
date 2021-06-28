from django.urls import path
from profiles_api import views

app_name='api'

urlpatterns =[
    path('', views.testApiView.as_view() ,name='testAPI')
]
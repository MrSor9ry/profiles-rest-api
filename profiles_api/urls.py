from django.urls import path, include

from rest_framework.routers import DefaultRouter

from profiles_api import views

router = DefaultRouter()
router.register('test-viewset', views.testViewSet, basename='test-viewset' )
router.register('profile', views.UserProfileViewSet)

app_name='api'

urlpatterns =[
    path('apiview/', views.testApiView.as_view() ,name='testAPI'),
    path('', include(router.urls)),
]
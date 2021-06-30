from django.urls import path, include

from rest_framework.routers import DefaultRouter

from profiles_api import views
app_name='api'

router = DefaultRouter()
router.register('test-viewset', views.testViewSet, basename='test-viewset' )
router.register('profile', views.UserProfileViewSet)
router.register('feed', views.UserProfileFeedViewSet)


urlpatterns =[
    path('apiview/', views.testApiView.as_view() ,name='testAPI'),
    path('login/', views.UserLoginApiView.as_view(), name='loginAPI'),
    path('', include(router.urls))

]
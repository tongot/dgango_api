from django.conf.urls import url
from django.conf.urls import include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register('hello-viewset', views.HellowViewSet, basename = ('hello-viewset'))
router.register('profile', views.UserProfileViewSet)

urlpatterns = [
    url('hello-view/', views.HelloApiView.as_view()),
    url('',include(router.urls))
]

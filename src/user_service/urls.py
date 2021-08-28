from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers

from user_service.viewsets import UserViewSet, HealthCheckView, GreetingsView, Test500View

router = routers.DefaultRouter()

router.register('user', UserViewSet)

urlpatterns = [
    path('', GreetingsView.as_view()),
    url('', include('django_prometheus.urls')),
    path('api/v1/', include(router.urls)),
    path('health', HealthCheckView.as_view()),
    path('handle500', Test500View.as_view()),
]
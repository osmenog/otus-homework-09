from django.urls import path, include
from rest_framework import routers

from user_service.viewsets import UserViewSet, HealthCheckView, GreetingsView

router = routers.DefaultRouter()

router.register('user', UserViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('', GreetingsView.as_view()),
    path('health', HealthCheckView.as_view())
]

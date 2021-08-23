from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from user_service.serializers import UserSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class HealthCheckView(APIView):
    def get(self, request):
        return Response({'ok': 'ok'})


class GreetingsView(APIView):
    def get(self, request):
        return Response({'greetings': 'user', 'headers': dict(request.headers)})

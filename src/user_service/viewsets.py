from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from user_service.serializers import UserSerializer

User = get_user_model()


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class HealthCheckView(APIView):
    def get(self, request):
        return Response({'ok': 'ok'})


class GreetingsView(APIView):
    def get(self, request):
        x = request.headers.get('X-Real-Ip')
        u = User.objects.filter(real_ip=x)
        if x and u.count():
            greetings = u.get().username
        else:
            greetings = 'Anonymous'
        return Response(f'Hello, {greetings}. Your IP: {x}')

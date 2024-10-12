from django.contrib.auth import authenticate
from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Employee
from .serializers import UserSerializer, EmployeeSerializer

class SignupView(generics.CreateAPIView):
    serializer_class = UserSerializer

class LoginView(generics.GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
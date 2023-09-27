from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import UpdateAPIView, CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.contrib.auth import login
from knox import views as knox_views

from .models import CustomUser
from .serializers import CreateUserSerializer, UpdateUserSerializer, LoginSerializer


# Create your views here.


# Pour créer un nouvel utilisateur
class CreateUserAPI(CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CreateUserSerializer
    permission_classes = (AllowAny,)


# Pour mettre à jour un compte utilisateur
class UpdateUserAPI(UpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UpdateUserSerializer


class LoginAPIView(knox_views.LoginView):
    permission_classes = (AllowAny, )
    serializer_class = LoginSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        # serializer = LoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.validated_data['user']
            login(request, user)
            response = super().post(request, format=None)
        else:
            return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

        return Response(response.data, status=status.HTTP_200_OK)

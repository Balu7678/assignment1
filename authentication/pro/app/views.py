from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions,generics
from django.contrib.auth.models import User
from .serializer import UserSerializer,RegisterSerializer
from knox.models import AuthToken
from rest_framework.authentication import SessionAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes,authentication_classes
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

class ListUsers(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        email = [user.email for user in User.objects.all()]
        return Response(email)

class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token = Token.objects.get_or_create(user=user)
        token=str(token)
        return Response({
            'token': token,
            'user_id': user.pk,
            'email': user.email
        })

class RegisterApi(APIView):
    serializer_class=RegisterSerializer
    def post(self,request,*args,**kwargs):
        serializer=RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        user = User.objects.get(username=request.data['username'])
        token = Token.objects.get(user=user)
        serilizer1 = UserSerializer(user)
        data={
            
            "user": serializer.data,
            "token": token.key
        }
        return Response(data,status=status.HTTP_201_CREATED)


class user_delete(APIView):
    authentication_classes = [authentication.TokenAuthentication,authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def post(self,request,*args,**kwargs):
        request.user.delete()
        request.user.auth_token.delete()
        return Response({
            "message": "user is successful delete"}
            )
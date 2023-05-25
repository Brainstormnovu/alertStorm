from django.contrib.auth import login, logout
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from rest_framework import status, generics, permissions
from .models import User
from .serializers import UserSerializer, RegisterSerializer, LoginSerializer, NotifySerializer
from .validations import clean_data


# Create your views here.

class WelcomeView(generics.GenericAPIView):
    """ returns welcome message """
    permission_classes = (permissions.AllowAny,)
    ##
    def get(self, request):
        return Response({'message': "Welcome to Our Weather App"}, status=status.HTTP_200_OK)


class UserListApiView(generics.ListCreateAPIView):
    """ filter api for admins """
    permission_classes = (permissions.IsAdminUser,)
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'country'

    search_fields = (
        '^country',
    )
    

class UserRegister(generics.GenericAPIView):
    """ register api view """
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        """ User sign up"""
        # print(f"Request data ==> {request.data}")
        data = clean_data(request.data)
        # print(f"Clean data ==> {data}")
        serializer = self.serializer_class(data=data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.create(data)
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
                
        



class UserLogin(generics.GenericAPIView):
    """
    Logs in an existing user.
    """
    permission_classes = (permissions.AllowAny,)
    serializer_class = LoginSerializer
    authentication_classes = (SessionAuthentication,)

    def post(self, request):
        """
        Checks is user exists.
        Email and password are required.
        Returns a JSON web token.
        """
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.validate(data)
            login(request, user)
            return Response(serializer.data, status=status.HTTP_200_OK)


class UserLogout(APIView):
    """ logout user """
    permission_classes = (permissions.IsAuthenticated, )

    def get(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)


class UserView(generics.GenericAPIView):
    """ User view """
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (SessionAuthentication, )

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response({'user': serializer.data}, status=status.HTTP_200_OK)



class NotifyTypeAPI(generics.GenericAPIView):
    """ Users choose their notification means """
    permission_classes = (permissions.IsAuthenticated, )
    authentication_classes = (SessionAuthentication, )
    serializer_class = NotifySerializer

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid(raise_exception=True):
            return Response(serializer.data, status=status.HTTP_200_OK)



    

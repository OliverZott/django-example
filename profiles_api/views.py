from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions


class HelloApiView(APIView):
    """Hello Api View"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns list of Api View features"""
        features = [
            'Uses HTTP methods as functions (get, post, put, patch, delete)',
            'Is similar to a traditional Django View',
            'Gives you most control over application logic',
            'Is mapped manually to URLs',
        ]

        return Response(
            {'message': 'Hello :)', 'api_features': features})  # gets dict or list (to be able to serialize as json)

    def post(self, request):
        """Create hello message with given name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name: str = serializer.validated_data.get('name')
            message: str = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):  # pk ... primary key
        """Handle updating an object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle a partial update of a object
        Only updates given fields... Put will overwrite all others with empty strings as well"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Deleting an object"""
        return Response({'method': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """
    Test ViewSet API
    Add functions, that represent actions you perform on typical API
    """
    serializer_class = serializers.HelloSerializer

    def list(self, request) -> Response:
        """Return hello message"""

        features = [
            'Uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLs using Routers',
            'Provides more functionality with less code',
        ]

        return Response({'message': 'ViewSet Features', 'features': features})

    def create(self, request):
        """Create a new hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name: str = serializer.validated_data.get('name')
            message: str = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Retriv a specific object by ID"""
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Handle updating an object"""
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handle updating part of an object"""
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handle removing an object"""
        return Response({'http_method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)  # defines how user will get authenticated
    permission_classes = (permissions.UpdateOwnProfile,)  # defines permissions user has

    # Filters for searching added
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


class UserLoginApiView(ObtainAuthToken):
    """handle creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


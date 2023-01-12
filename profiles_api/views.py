from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Hello Api View"""

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

from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """Serializers a name field for testing API view"""

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    name = serializers.CharField(max_length=10)
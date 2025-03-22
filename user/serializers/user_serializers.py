from rest_framework import serializers
from user.models import User


class UserSerializer(serializers.Serializer):
    name = serializers.CharField()

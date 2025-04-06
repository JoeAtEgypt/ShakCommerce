from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from user.models import User


class UserSerializer(serializers.Serializer):
    name = serializers.CharField()


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "phone_number", "password")

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED

from user.models import User
from user.serializers import UserSerializer
from user.serializers.user_serializers import RegisterSerializer


class UserAPI(APIView):
    # permission_classes = []
    # authentication_classes = []

    def get(self, request):
        data = UserSerializer().data
        res = {"user": data}
        return Response(res, status=HTTP_200_OK)


class RegisterAPI(APIView):
    @staticmethod
    def post(request):
        user = RegisterSerializer(data=request.data)

        # validate user
        user.is_valid(raise_exception=True)

        # sending OTP to an email

        # Create User
        user.save()

        return Response(status=HTTP_201_CREATED)

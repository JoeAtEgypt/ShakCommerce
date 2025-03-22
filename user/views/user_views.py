from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from user.models import User
from user.serializers import UserSerializer

# from django_filters import rest_framework as filters
# from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, DestroyAPIView


class UserAPI(APIView):
    # permission_classes = []
    # authentication_classes = []

    def get(self, request):
        data = UserSerializer().data
        res = {"user": data}
        return Response(res, status=HTTP_200_OK)

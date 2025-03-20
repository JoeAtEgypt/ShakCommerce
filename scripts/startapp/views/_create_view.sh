create_view () {
  cat <<EOF
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from $app_name.models import $app_name_class
from $app_name.serializers import ${app_name_class}Serializer
# from django_filters import rest_framework as filters
# from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, DestroyAPIView

class ${app_name_class}API(APIView):
    # permission_classes = []
    # authentication_classes = []

     def get(self, request):
        data = ${app_name_class}Serializer().data
        res = {"${app_name}": data}
        return Response(res, status=HTTP_200_OK)
EOF
}

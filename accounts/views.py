from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *


class SignupAPIView(APIView):
    http_method_names = ['post']
    permission_classes = (permissions.AllowAny,)


    def post(self, *args, **kwargs):
        serializer = UserSerializer(data=self.request.data)

        if serializer.is_valid():
            get_user_model().objects.create_user(**serializer.validated_data)
            return Response(status=status.HTTP_201_CREATED)
        return Response(
            status=status.HTTP_400_BAD_REQUEST,
            data={'errors': serializer.errors}
        )
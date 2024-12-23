from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from webapp.serializers import PasswordResetSerializer


class PasswordResetView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        access_token = request.headers.get('Authorization').split(' ')[1]

        serializer = PasswordResetSerializer(data=request.data)
        if serializer.is_valid():####
            user = serializer.save(validated_data=serializer.validated_data, access_token=access_token)
            return Response({"detail": "Password successfully reset."}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from rest_framework import status
from rest_framework.response import Response
from apps.student.serializers import ListStudentSerializer, StudentSerializer
from apps.user.models import User
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAdminUser


class StudentListApi(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        students = User.objects.filter(user_type=1)
        serializer = ListStudentSerializer(students, many=True)
        return Response({"students": serializer.data}, status=status.HTTP_200_OK)


class CreateStudentApi(APIView):
    permission_classes = (IsAuthenticated, IsAdminUser)

    def post(self, request, *args, **kwargs):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

class UpdateStudentApi(APIView):
    permission_classes = (IsAuthenticated, IsAdminUser)

    def put(self, request, pk, *args, **kwargs):
        student = get_object_or_404(User, pk=pk, user_type=1)
        serializer = StudentSerializer(student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

class DeleteStudentApi(APIView):
    permission_classes = (IsAuthenticated, IsAdminUser)

    def delete(self, request, pk, *args, **kwargs):
        student = get_object_or_404(User, pk=pk, user_type=1)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

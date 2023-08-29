from rest_framework import status
from rest_framework.response import Response
from apps.user.models import User
from rest_framework.views import APIView
from apps.lesson.models import Lesson
from apps.lesson.models import Note
from apps.lesson.serializers import LessonSerializer
from apps.lesson.serializers import NoteSerializer
from rest_framework.permissions import IsAuthenticated

class LessonListApi(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        lessons = Lesson.objects.all()
        student = self.request.query_params.get('student')
        if student:
            lessons = lessons.filter(user__username=student)
        serializer = LessonSerializer(lessons, many=True)
        return Response({"lessons": serializer.data}, status=status.HTTP_200_OK)


class NoteListApi(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        motes = Note.objects.all()
        student = self.request.query_params.get('student')
        lesson_name = self.request.query_params.get('lesson_name')

        if student:
            motes = motes.filter(user__username=student)

        if lesson_name:
            motes = motes.filter(lesson__name=lesson_name)

        serializer = NoteSerializer(motes, many=True)
        return Response({"motes": serializer.data}, status=status.HTTP_200_OK)

from rest_framework import serializers
from apps.lesson.models import Lesson
from apps.lesson.models import Note
from apps.student.serializers import StudentSerializer

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ("name", "teacher_name", "period_information")



class NoteSerializer(serializers.ModelSerializer):
    student = StudentSerializer()
    lesson = LessonSerializer()
    class Meta:
        model = Note
        fields = ("user", "lesson", "grade_value", 'created_date')

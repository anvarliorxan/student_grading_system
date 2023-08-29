from rest_framework import serializers
from apps.user.models import User


class ListStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "name", "surname", "birth_date")


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "password", "name", "surname", "birth_date")


    def create(self, validated_data):
        student = User.objects.create(
            username=validated_data['username'],
            password=validated_data['password'],
            name=validated_data['name'],
            surname=validated_data['surname'],
            birth_date=validated_data['birth_date'],
            user_type=1
        )
        return student

    def put(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.password = validated_data.get('password', instance.password)
        instance.name = validated_data.get('name', instance.name)
        instance.surname = validated_data.get('surname', instance.surname)
        instance.birth_date = validated_data.get('birth_date', instance.birth_date)
        return instance
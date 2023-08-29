from django.db import models


class Lesson(models.Model):
    user = models.ManyToManyField('user.User')
    name = models.CharField(max_length=55)
    teacher_name = models.CharField(max_length=55)
    period_information = models.TextField()

    def __str__(self):
        return self.name


class Note(models.Model):
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='notes')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='notes')
    grade_value = models.PositiveIntegerField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.name


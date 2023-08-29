from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class UserAccountManager(BaseUserManager):

    def create_user(self, username, password=None):
        if not username:
            raise ValueError('Users must provide a username to create an account')

        user = self.model(
            username=username
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password, email=None):

        user = self.create_user(
            username=username,
            password=password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save(using=self._db)
        return user


class User(AbstractUser):

    USER_TYPE_CHOICES = (
        (1, 'student'),
        (2, 'manager'),
        (3, 'admin'),
    )
    username = models.CharField(max_length=150, unique=True, null=True, blank=True)
    name = models.CharField(max_length=150, null=True, blank=True)
    surname = models.CharField(max_length=150, null=True, blank=True)
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, null=True, blank=True, default=1)
    created_date = models.DateTimeField(auto_now_add=True)
    birth_date = models.DateField(null=True, blank=True)

    objects = UserAccountManager()


    def __str__(self):
        return self.username




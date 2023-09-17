from django.contrib.auth import get_user_model
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    def create_user(self, email, nickname, birthdate, password, **extra_fields):
        fields = list()

        if not email:
            fields.append('email')
        if not nickname:
            fields.append('nickname')
        if not birthdate:
            fields.append('birthdate')

        if fields:
            field_required = ''

            for i in range(len(fields)):
                field_required += fields[i]
                if i != len(fields) - 1:
                    field_required += ', '

            raise ValueError(_(f'The following fields must be set: {field_required}'))

        email = self.normalize_email(email)

        if get_user_model().objects.filter(email=email):
            raise ValueError(_('User with this Email already exists.'))
        
        if get_user_model().objects.filter(nickname=nickname):
            raise ValueError(_('User with this nickname already exists.'))

        user = self.model(email=email, nickname=nickname, birthdate=birthdate, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    

    def create_superuser(self, email, nickname, birthdate, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if not extra_fields.get('is_staff'):
            raise ValueError(_('Superuser must have is_staff=True.'))
        if not extra_fields.get('is_superuser'):
            raise ValueError(_('Superuser must have is_superuser=True'))

        return self.create_user(
            email=email,
            nickname=nickname,
            birthdate=birthdate,
            password=password,
            **extra_fields
        )


class User(AbstractUser):
    email = models.EmailField(unique=True)
    nickname = models.CharField(max_length=8, unique=True)
    birthdate = models.DateField()
    objects = UserManager()
    REQUIRED_FIELDS = ['email', 'nickname', 'birthdate']


    def __str__(self):
        return self.nickname
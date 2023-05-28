from django.db import models
from django.utils import timezone
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)
from django_enum import EnumField
from uuid import uuid4
from multiselectfield import MultiSelectField


class UserManager(BaseUserManager):
    def _create_user(self, email, password=None, **extra_fields):
        """ creates and saves a User
        """
        if not email:
            raise ValueError('User must have an email address')
        
        user = self.model(
            email=self.normalize_email(email),
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        print(f"User ==> {user}")
        return user
    
    def create_user(self, email, password=None, **extra_fields):
        """
        Create and return a `User` with an email, username and password.
        """
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('city', 'Lagos')
        extra_fields.setdefault('country', 'Nigeria')

        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and return a `User` with superuser (admin) permissions.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('city', 'Lagos')
        extra_fields.setdefault('country', 'Nigeria')

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    """User Model"""
    userid = models.UUIDField(default=uuid4, editable=False)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255, null=False)
    date_joined = models.DateTimeField(default=timezone.now)
    city = models.CharField(max_length=255, null=False, default="Lagos")
    country = models.CharField(max_length=255, null=False, default="Nigeria")
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['userid','password', 'city', 'country']
    objects = UserManager()

    def __str__(self) -> str:
        return self.email


class Notification(models.Model):
    """ Notification options """
    NOTIFY_CHOICES=(
        ('1', "In-App"),
        ("2", "Push"),
        ("3", "Email"),
        ("4", "Chat"),
        ("5", "SMS"),
    )

    user = models.ForeignKey(User, related_name='notifications', on_delete=models.CASCADE)
    notification = MultiSelectField(choices=NOTIFY_CHOICES, max_length=5, max_choices=5)

    class Meta:
        unique_together = ['user', 'id']
        ordering = ['id']

    def __str__(self) -> str:
        return f"{self.id}: {self.notification}"

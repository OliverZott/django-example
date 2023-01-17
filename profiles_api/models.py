from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email: int, name: str, password=None):  # error "int"
        """Create new user profile"""

        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        user.set_password(password)

        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password):
        """Create new superuser with given details"""

        user = self.create_user(email, name, password)
        user.is_superuser = True  # comes from Mixin (PermissionsMixin)
        user.is_staff = True

        user.save(using=self._db)
        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """
    Database model for users in the system
    Together with manager used to create users via Django CLI
    """

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    # overwrite default username with email field
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Retrieve full user name"""
        return self.name

    def get_short_name(self):
        """Retrieve short name of user"""
        return self.name

    def __str__(self):
        """Return string representation of the user"""
        return self.email


class ProfileFeedItem(models.Model):
    """Profile status update"""

    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # to avoid hard-coding, use the user-model from settings.py
        on_delete=models.CASCADE
    )

    status_text = models.CharField(max_length=255)

    created_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return model as string"""
        return self.status_text

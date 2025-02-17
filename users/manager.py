from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin, BaseUserManager
)
from django.db import transaction

class UserManager(BaseUserManager):
    def _create_user(self, email, password, extra_fields):
        """
    Creates and saves a User with the given email, and password.
"""
        if not email:
            raise ValueError('The given email must be correct')
        try:
            with transaction.atomic():
                user = self.model(email=email, **extra_fields)
                user.set_password(password)
                user.save(using=self._db)
                return user
        except:
            raise

    def create_user(self, email, password=None, **extrafields):
        extrafields.setdefault('is_staff', False)
        extrafields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extrafields)
    

    def create_superuser(self, email,password=None, **extrafields):
        extrafields.setdefault('is_staff', True)
        extrafields.setdefault('is_superuser', True)
        return self._create_user(email,password, **extrafields)

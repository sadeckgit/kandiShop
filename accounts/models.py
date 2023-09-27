from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.


class UserManger(BaseUserManager):

    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("The email is not given...")
        else:
            email = self.normalize_email(email)
            user = self.model(email=email, **extra_fields)
            user.is_active = True
            user.set_password(password)
            user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if not extra_fields.get('is_staff'):
            raise ValueError("Superuser must be have 'is_staff = True'")

        if not extra_fields.get('is_superuser'):
            raise ValueError("Superuser must have 'is_superuser = True'")
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser):

    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    phone = models.IntegerField(null=True)
    email = models.EmailField(max_length=250, unique=True)
    password = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone']

    objects = UserManger()

    def __str__(self):
        return self.email

    def ha_module_perms(self, app_label):
        return True

    def has_perms(self, perm, obj=None):
        return True

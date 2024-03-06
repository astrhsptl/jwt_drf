from django.db import models
from django.contrib.auth.models import (
	AbstractBaseUser, BaseUserManager,
)


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **other_fields):
        if email is None:
            raise TypeError("Users must have an email address.")


        user = self.model(email=self.normalize_email(email))
        
        for field, value in other_fields.items():
            if hasattr(user, field):
                setattr(user, field, value)

        user.set_password(password)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password, username="admin"):
        if password is None:
            raise TypeError("Superusers must have a password.")

        user = self.create_user(email=email, password=password, username=username)
        user.is_superuser = True
        user.is_staff = True
        user.private_access = True
        user.save()

        return user

class User(AbstractBaseUser):
    id = models.AutoField(primary_key=True)

    # base information
    last_login = None

    username = models.CharField(verbose_name="Username", max_length=50, blank=False, unique=True)
    avatar = models.ImageField(verbose_name="Avatar", blank=True, upload_to="user/avatar")
    email = models.EmailField(verbose_name="Email", max_length=150, blank=False, unique=True)

    # permission information
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    # Auth settings
    USERNAME_FIELD = "email"

    objects: UserManager = UserManager()

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser

    def __str__(self):
        return self.email

    class Meta:
        indexes = [
            models.Index(fields=["id"], name="id_index"),
        ]

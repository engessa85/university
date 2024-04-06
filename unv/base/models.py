from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models

class UserAccountManager(BaseUserManager):
    def create_user(self, username, email, password=None, civilID=None):

        user = self.model(
            username=username,
            email=self.normalize_email(email),
            civilID=civilID
        )


        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, email, password=None, civilID=None):
        user = self.create_user(
            username=username,
            email=email,
            password=password,
            civilID=civilID
        )

        user.is_active = True
        user.is_staff = True
        user.is_superuser = True

        user.is_student = True
        user.is_university = True

        user.save(using=self._db)
        return user

class UserAccount(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    civilID = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_university = models.BooleanField(default=False)
    
    objects = UserAccountManager()

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email', 'civilID']


    def get_full_name(self):
        return self.email
    
    def get_short_name(self):
        return self.email
    
    def __str__(self):
        return self.email
    

class UniversityUser(UserAccount):
    universityname = models.CharField(max_length=255, blank=True, null=True)
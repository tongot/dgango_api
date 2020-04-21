from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """work with user custom user model """

    def create_user(self, email, name, password=None):

        if not email:
            raise ValueError('user email must be provided')

        email=self.normalize_email(email)
        user= self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self,email,name,password):
        """create a new user with the new given details"""
        user = self.create_user(email,name,password)

        user.is_superuser=True
        user.is_staff= True

        user.save(using=self._db)

class UserProfile(AbstractBaseUser,PermissionsMixin):
    """Represents a user Profile inside our system"""


    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    #object manager used to do other functions to our profile 
    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """"used to get users full name"""

        return self.name

    def get_short_name(self):
        """"used to get users short name """

        return self.name

    def __str__(self):
        """convert object to string"""

        return self.email
class ProfileFeedItem(models.Model):
    """profile status update"""

    user_profile = models.ForeignKey('UserProfile', on_delete = models.CASCADE)
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        '''return model as string'''
        return self.status_text

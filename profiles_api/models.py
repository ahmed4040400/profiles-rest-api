from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
# allow us to retrieve the setting components from the
# project wide setting.py file
from django.conf import settings


class UserProfileManager(BaseUserManager):
    """manage the user profile
       like adding users and super users
     """

    def creat_user(self, email, name, password=None):
        """create a normal user"""
        if not email:
            raise ValueError("the user must have an email")
        # normalize_email() to make the second half of the email
        # not case sensitive
        email = self.normalize_email(email)
        # adding the name and the emails to the model
        # which in this case is the UserProfile model
        user = self.model(email=email, name=name)
        # adding the password to the model using the
        # set_password method
        user.set_password(password)
        # saving the user object and specify the using is optional
        # incas we're using multiple dbs
        user.save(using=self._db)
        # returns the user object
        return user

    def creat_superuser(self, email, password, name):
        """for creating a super user"""
        # start by creating a normal user
        user = self.creat_user(email, name, password)
        # then add the required permissions to be a super user
        # note : the supper user permissions is automaticly created
        # the the PermissionsMixin
        user.is_superuser = True
        user.is_staff = True
        # and then save the user
        user.save(using=self._db)
        # and then return the user
        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """database model for user in the system"""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    # is admin
    is_staff = models.BooleanField(default=False)
    # referring the user profile manager
    # that's gonna handle creating users
    objects = UserProfileManager()
    # replacing the username field with the email field
    # by class variable USERNAME_FIELD
    # that way we're gonna use the email to login instate of the username
    USERNAME_FIELD = 'email'
    # the REQUIRED_FIELDS to add some required field to the
    # sign up process in this case we're only adding name field
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        # TODO:returns the user full name
        return self.name

    def get_short_name(self):
        # TODO:returns the user short name
        return self.name

    # for preview the users based on the email adress
    def __str__(self):
        return self.name


# the users feed a model that receive posts from user,
# a model made for posts
class ProfileFeedItem(models.Model):
    # the models.ForeignKey() is a way to connect a model with another one
    # that allow us to refer to the user that published that post
    user_profile = models.ForeignKey(
        # the 1st argument is for the model name
        # we could've just put a string of the model name
        # but in this case we are referring to a model that
        # handle the authentication system ,
        # so it's a good practice to refer to it
        # by getting it from the setting AUTH_USER_MODEL
        settings.AUTH_USER_MODEL,
        # define what would happen if the model associated model
        # got deleted , well in this case we tell it to CASCADE
        # which means to delete the user feed as wel
        on_delete=models.CASCADE
    )
    # a field for the feed content
    status_text = models.CharField(max_length=255)
    # the date of the feed
    # auto_now_add allow the that dateField to take the current time
    # of the feed without bother the user with asking him to enter it
    create_on = models.DateTimeField(auto_now_add=True)

    # the string representation
    def __str__(self):
        return self.status_text

from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import  BaseUserManager


class UserProfileManager(BaseUserManager):
    """manage the user profile
       like adding users and super users
     """

    def create_user(self , email,name,password=None):

        """creat a normal user"""
        if not email :
            raise ValueError("the user must have an email")
        # to make the second half of the email not case senstive
        email = self.normalize_email(email)
        #adding the name and the emails to the model
        #which in this case is the UserProfile model
        user = self.model(email = email , name = name)
        #adding the password to the model using the
        #set_password method
        user.set_password(password)
        #saving the user object and specify the using is optional
        #incase we're using multiple dbs
        user.save(using = self._db)
        #returns the user object
        return user

    def create_superuser(self ,email,password,name):
        """for creating a super user"""
        # start by creating a normal user
        user = self.creat_user(email,name,password)
        #then add the required permissions to be a super user
        # note : the supper user permissions is automaticly created
        #the the PermissionsMixin
        user.is_superuser = True
        user.is_staff = True
        #and then save the user
        user.save(using = self._db)
        #and then return the user
        return user




class UserProfile(AbstractBaseUser , PermissionsMixin):
    """database model for user in the system"""

    email = models.EmailField(max_length = 255 ,unique = True )
    name = models.CharField(max_length= 255,unique =True)
    is_active = models.BooleanField(default = True)
    #is admin
    is_staff = models.BooleanField(default = False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        #TODO:returns the user full name
        return self.name

    def get_short_name(self):
        #TODO:returns the user short name
        return self.name

    #for preview the users based on the email adress
    def __str__(self):
        return self.name

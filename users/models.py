from django.db import models
from mongoengine import *
from datetime import datetime
import os
import json
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

connect(
    db= "Form2",
    username= "Tanmay1903",
    password= "Tanmaymongodb",
    host='mongodb+srv://Tanmay1903:Tanmaymongodb@intern-9eye-at0b4.mongodb.net/Form2?retryWrites=true&w=majority',
)

class UserManager(BaseUserManager):
    def create_user(self, email,username, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have an username')

        user = self.model(
            email=self.normalize_email(email),
            username=username
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email,username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
        )
        user.is_staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email,username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
        )
        user.is_staff = True
        user.is_admin = True
        user.is_superuser=True
        user.save(using=self._db)
        return user

class custom_user(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    username = models.CharField(max_length=50,unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        #"Does the user have a specific permission?"
        return True

    def has_module_perms(self, app_label):
        #"Does the user have permissions to view the app `app_label`?"
        return True
'''
class UserManager(BaseUserManager):
    def create_user(self, email,username, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have an username')

        user = self.model(
            email=self.normalize_email(email),
            username=username
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email,username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
        )
        user.is_staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email,username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
        )
        user.is_staff = True
        user.is_admin = True
        user.is_superuser=True
        user.save(using=self._db)
        return user

class custom_user(AbstractBaseUser):
    email = EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    username = StringField(max_length=50,unique=True)
    is_active = BooleanField(default=True)
    is_staff = BooleanField(default=False)
    is_admin = BooleanField(default=False)
    is_superuser = BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        #"Does the user have a specific permission?"
        return True

    def has_module_perms(self, app_label):
        #"Does the user have permissions to view the app `app_label`?"
        return True
'''
#disconnect()

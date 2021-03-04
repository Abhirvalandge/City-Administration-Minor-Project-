from django.db import models
from django.conf import settings
from django.utils import timezone
from datetime import datetime

class RegistrationDataModel(models.Model):
    name = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    fname = models.CharField(max_length=20)
    f_lname = models.CharField(max_length=20)
    dob = models.DateField()
    gender = models.CharField(max_length=1)
    nationality = models.CharField(max_length=1)

    # Address Details
    houseno = models.IntegerField()
    address = models.CharField(max_length=30)
    city = models.CharField(max_length=10)
    pin = models.IntegerField()
    state = models.CharField(max_length=20)
    district = models.CharField(max_length=20)

    # Contact Details
    mobileno = models.IntegerField()
    emailid = models.EmailField(primary_key=True)
    password = models.CharField(max_length=10)

class ShareIdeaModel(models.Model):
    s_name = models.CharField(max_length=20)
    s_address = models.CharField(max_length=30)
    s_email = models.EmailField(primary_key=True)
    s_mobile = models.IntegerField()
    s_message = models.CharField(max_length=1000)
    s_publish = models.DateTimeField(default=datetime.now(),blank=True)


class CompIssueModel(models.Model):
    com_name = models.CharField(max_length=20)
    com_address = models.CharField(max_length=30)
    com_email = models.EmailField(primary_key=True)
    com_mobile = models.IntegerField()
    com_image = models.FileField(upload_to='complaint_issue/')
    com_message = models.CharField(max_length=1000)
    com_publish = models.DateTimeField(default=datetime.now())
    #com_problem = models.CharField(max_length=1)


class GiveSuggestionModel(models.Model):
    g_name = models.CharField(max_length=20)
    g_projectname = models.TextField(max_length=1000)
    g_address = models.CharField(max_length=30)
    g_email = models.EmailField(primary_key=True)
    g_mobile = models.IntegerField()
    g_message = models.CharField(max_length=1000)
    g_publish = models.DateTimeField(default=datetime.now())


class PublishProjectModel(models.Model):
    project_name = models.CharField(max_length=30,primary_key=True)
    project_image = models.FileField(upload_to='publishproject/')

class ProfileImageModel(models.Model):
    reg_profile = models.FileField(upload_to='reg_profile/')


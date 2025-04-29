# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    email = models.CharField(max_length=255, null=True, blank=True)
    role = models.CharField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Checklistitem(models.Model):

    #__Checklistitem_FIELDS__
    title = models.CharField(max_length=255, null=True, blank=True)
    descreption = models.TextField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=255, null=True, blank=True)
    is_completed = models.BooleanField()
    notes = models.TextField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(blank=True, null=True, default=timezone.now)
    updated_at = models.DateTimeField(blank=True, null=True, default=timezone.now)
    oder = models.IntegerField(null=True, blank=True)

    #__Checklistitem_FIELDS__END

    class Meta:
        verbose_name        = _("Checklistitem")
        verbose_name_plural = _("Checklistitem")


class Company(models.Model):

    #__Company_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    address = models.TextField(max_length=255, null=True, blank=True)

    #__Company_FIELDS__END

    class Meta:
        verbose_name        = _("Company")
        verbose_name_plural = _("Company")


class User(models.Model):

    #__User_FIELDS__
    email = models.TextField(max_length=255, null=True, blank=True)
    role = models.CharField(max_length=255, null=True, blank=True)

    #__User_FIELDS__END

    class Meta:
        verbose_name        = _("User")
        verbose_name_plural = _("User")


class Request(models.Model):

    #__Request_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(max_length=255, null=True, blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    responsable = models.ForeignKey(User, on_delete=models.CASCADE)
    consultant = models.ForeignKey(User, on_delete=models.CASCADE)
    statut = models.CharField(max_length=255, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    due_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    created_at = models.DateTimeField(blank=True, null=True, default=timezone.now)
    updated_at = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Request_FIELDS__END

    class Meta:
        verbose_name        = _("Request")
        verbose_name_plural = _("Request")



#__MODELS__END

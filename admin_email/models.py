from django.db import models

from mptt.models import MPTTModel, TreeForeignKey
from annoying.fields import AutoOneToOneField

class Configuration(models.Model):
    user = AutoOneToOneField('auth.User')

    host = models.CharField(max_length=255, null=True, blank=True)
    port = models.IntegerField(default=993)
    username = models.CharField(max_length=255, null=True, blank=True)
    password = models.CharField(max_length=255, null=True, blank=True)

class Email(MPTTModel):
    subject = models.CharField(max_length=255, blank=True, null=True)
    parent = TreeForeignKey('Email', null=True, blank=True, related_name='children')
    sender = models.ForeignKey('auth.User', null=True, blank=True, related_name='emails')
    to = models.ManyToManyField('Address', null=True, blank=True, related_name='email_set_as_to')
    cc = models.ManyToManyField('Address', null=True, blank=True, related_name='email_set_as_cc')
    bcc = models.ManyToManyField('Address', null=True, blank=True, related_name='email_set_as_bcc')
    text = models.TextField(null=True, blank=True)
    html = models.TextField(null=True, blank=True)

class Address(models.Model):
    address = models.EmailField()

class Attachement(models.Model):
    email = models.ForeignKey('Email')
    media = models.FileField(upload_to='admin-email/attachements')

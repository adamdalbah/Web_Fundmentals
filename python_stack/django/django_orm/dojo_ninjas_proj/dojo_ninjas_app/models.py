from typing import Text
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, DateTimeField

class Dojo(models.Model):
    name = CharField(max_length=255)
    city = CharField(max_length=255)
    state = CharField(max_length=255)
    desc = CharField(max_length=255)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

class Ninja(models.Model):
    first_name = CharField(max_length=255)
    last_name = CharField(max_length=255)
    dojo = models.ForeignKey(Dojo, related_name = 'ninjas', on_delete=CASCADE)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
# Create your models here.

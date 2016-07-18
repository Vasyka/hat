# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user= models.OneToOneField(User)
    avatar= models.ImageField(upload_to='Images/users', verbose_name='Image')
    rating=models.IntegerField(default=0)
    karma=models.IntegerField(default=0)

    def __unicode__(self):
        return unicode(self.user)

class Room(models.Model):
    title=models.CharField(max_length=63,default='test')
    time_creation=models.DateTimeField('Time of room creation')
    users=models.ManyToManyField(UserProfile)
    
    def __unicode__(self):
        return unicode(self.title)
    
class Game(models.Model):
    title=models.CharField(max_length=63,default='test')
    room=models.ForeignKey(Room)
    time_creation=models.DateTimeField('Time of creation')

    def __unicode__(self):
        return unicode(self.title)

class SecretWord(models.Model):
    word=models.CharField(max_length=255)
    game=models.ForeignKey(Game)
    
    def __unicode__(self):
        return unicode(self.word)

class UserRole(models.Model):
    PLAYER = 'PL'
    LIDER = 'LID'
    ROLE_CHOICES = (        
        (LIDER, 'Lider'),
   	(PLAYER, 'Player'),
    )
    user=models.ForeignKey(UserProfile)
    game=models.ForeignKey(Game)
    role = models.CharField(max_length=3,choices=ROLE_CHOICES,default=LIDER)
    
    def __unicode__(self):
        return unicode(self.role)

class Message(models.Model):
    text=models.TextField(max_length=2047)
    time_creation=models.DateTimeField('Time of room creation')
    room=models.ForeignKey(Room)
    user=models.ForeignKey(UserProfile)
    user_role=models.ForeignKey(UserRole)

    def __unicode__(self):
        return unicode(self.text)


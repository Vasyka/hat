# -*- coding: utf-8 -*-
from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import UserProfile, Room, Game, SecretWord, UserRole, Message
 
class UserInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'More information'
 
class UserAdmin(UserAdmin):
    inlines = (UserInline, )

class RoomAdmin(admin.ModelAdmin):
    list_display=('title','time_creation')
    list_filter = ['time_creation']

class GameAdmin(admin.ModelAdmin):
    list_display=('title','time_creation','room')
    list_filter = ['time_creation','room']

class SecretWordAdmin(admin.ModelAdmin):
    list_display=('word','game')
    list_filter = ['game']

class UserRoleAdmin(admin.ModelAdmin):
    list_display=('user','game','role')
    list_filter = ['user','game']

class MessageAdmin(admin.ModelAdmin):
    list_display=('text','time_creation','room','user','user_role')
    list_filter = ['time_creation','room','user']

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Room,RoomAdmin)
admin.site.register(Game,GameAdmin)
admin.site.register(SecretWord,SecretWordAdmin)
admin.site.register(UserRole,UserRoleAdmin)
admin.site.register(Message,MessageAdmin)

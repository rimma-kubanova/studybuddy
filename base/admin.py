from django.contrib import admin

# Register your models here.

from .models import Room, Topic, Message

admin.site.register(Room) #registering model
admin.site.register(Topic)
admin.site.register(Message)
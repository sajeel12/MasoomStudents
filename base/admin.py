from django.contrib import admin

# Register your models here.

from .models import Room, Message, Topic, User

admin.site.register(User)
admin.site.register(Room)
admin.site.register(Message)
admin.site.register(Topic)

admin.site.site_header = "__Masoom__ Admin"
admin.site.site_title = "__Masoom__ Admin Portal"
admin.site.index_title = "__Masoom__  Nizame-e-Alam"
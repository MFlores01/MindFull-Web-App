from django.contrib import admin
from .models import JournalEntry
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

admin.site.register(JournalEntry)

#from django.contrib.auth.models import User
admin.site.register(CustomUser, UserAdmin)
#admin.site.register(User)
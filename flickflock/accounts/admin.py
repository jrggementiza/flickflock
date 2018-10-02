from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import CustomUser, Group, Membership
from flockstream.models import Photo

admin.site.register(CustomUser, UserAdmin)
admin.site.register(Group)
admin.site.register(Membership)
admin.site.register(Photo)

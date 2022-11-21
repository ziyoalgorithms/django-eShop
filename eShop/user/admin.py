from django.contrib import admin

from user.models import UserAcc, UserAccProfile


admin.site.register(UserAcc)
admin.site.register(UserAccProfile)

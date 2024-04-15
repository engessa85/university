from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import UniversityUser, StudentMoreInfo, UniversityData
User = get_user_model()

admin.site.register(User)
admin.site.register(UniversityUser)
admin.site.register(StudentMoreInfo)
admin.site.register(UniversityData)

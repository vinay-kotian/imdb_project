from django.contrib import admin

# Register your models here.

from models import GenreCategory
from models import MovieDetails
from models import UserProfile

admin.site.register(GenreCategory)
admin.site.register(MovieDetails)
admin.site.register(UserProfile)
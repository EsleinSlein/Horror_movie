from django.contrib import admin

from .models import Movies


class MoviesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


admin.site.register(Movies)

# Register your models here.

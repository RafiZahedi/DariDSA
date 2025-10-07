from django.contrib import admin
from .models import Lesson
# Register your models here.


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'content')
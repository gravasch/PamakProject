from django.contrib import admin
from .models import TodoItem
from tinymce.widgets import TinyMCE
from django.db import models

# Register your models here.


class TodoAdmin(admin.ModelAdmin):

	fieldsets = [
		("Date", {"fields": ["published"]}),
		("Content", {"fields": ["content"]}),
		]

	formfield_overrides = {
		models.TextField: {'widget': TinyMCE()}
	}


admin.site.register(TodoItem, TodoAdmin)

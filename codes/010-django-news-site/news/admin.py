from django.contrib import admin
from .models import Post
# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	list_display = ("title", "is_active", "user", "date",)
	search_fields = ("title", "user__username",)
	list_filter = ("is_active",)
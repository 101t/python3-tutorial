from django.contrib import admin

# Register your models here.
from .models import Tag, Article

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
	list_display = ("name",)
	search_fields = ("name",)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
	list_display = ("title", "user", "tags_display", "is_active", "state", "created",)
	list_filter = ("state", "created",)
	search_fields = ("title", "user__username", "user__first_name", "user__last_name", "user__email",)
	def tags_display(self, obj):
		return ", ".join([tag.name for tag in obj.tags.all()])
	tags_display.short_description = "Tags"
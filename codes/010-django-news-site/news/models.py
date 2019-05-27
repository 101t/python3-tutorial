from django.db import models
from django.contrib.auth.models import User

from autoslug import AutoSlugField

class Post(models.Model):
	class Meta:
		verbose_name = "Post"
		verbose_name_plural = "Posts"
	title = models.CharField(verbose_name="Title", max_length=155)
	slug  = AutoSlugField(populate_from='title', unique_with=['title'])
	body  = models.TextField(verbose_name="Description")
	user  = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Publisher") # Django 2.x > required
	date  = models.DateTimeField("Published Date")
	is_active = models.BooleanField("Is Published", default=False)

	def __str__(self):
		return self.title

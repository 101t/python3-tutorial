from django.db import models
from django.contrib.auth.models import User

from main.utils import TimeStampedModel

from autoslug import AutoSlugField

class Tag(models.Model):
	class Meta:
		verbose_name = "Tag"
		verbose_name_plural = "Tags"
		ordering = ("name",)
	name = models.CharField(verbose_name="Name", max_length=32, unique=True)
	slug  = AutoSlugField(populate_from='name', unique=True)
	def __str__(self):
		return self.name

class Article(TimeStampedModel):
	class Meta:
		verbose_name = "Article"
		verbose_name_plural = "Articles"
		ordering = ("-created",)
	PENDING = "pending"
	DRAFT = "draft"
	APPROVED = "approved"
	CANCELED = "canceled"
	STATES = (
		(PENDING, "Pending",),
		(DRAFT, "Draft",),
		(APPROVED, "Approved",),
		(CANCELED, "Canceled",),
	)
	title = models.CharField(verbose_name="Title", max_length=250)
	slug  = AutoSlugField(populate_from='title', unique=True)
	body = models.TextField(verbose_name="Text")
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	is_active = models.BooleanField(verbose_name="Is Active", default=False)
	state = models.CharField(verbose_name='State', default=PENDING, choices=STATES, max_length=24)
	tags = models.ManyToManyField(Tag, blank=True, related_name="tags",)

	def __str__(self):
		return self.title
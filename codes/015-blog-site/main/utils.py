from django.db import models

class TimeStampedModel(models.Model):
	class Meta:
		abstract = True
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	def get_dict(self):
		return dict(
			created=self.created,
			modified=self.modified,
		)
	def isedited(self):
		return self.created.strftime('%Y-%m-%d %H:%M:%S') == self.modified.strftime('%Y-%m-%d %H:%M:%S')
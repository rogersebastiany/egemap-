from django.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class produto(models.Model):
	produtoid = models.IntegerField(default=0)
	produtonome = models.CharField(max_length=200)
	produtopreco = models.IntegerField(default=0)
	def __str__(self):
		return self.produtonome

@python_2_unicode_compatible
class cliente(models.Model):
	clienteid = models.IntegerField(default=0)
	clientenome = models.CharField(max_length=200)
	def __str__(self):
		return self.clientenome

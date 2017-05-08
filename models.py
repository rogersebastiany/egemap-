from django.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class usuarios(models.Model):
	usuarioid = models.AutoField(primary_key=True)
	usuariologin = models.CharField(max_length=10)
	usuariopasswd = models.CharField(max_length=10)
	usuarionome = models.CharField(max_length=30)
	def __str__(self):
		return self.usuariologin

@python_2_unicode_compatible
class clientes(models.Model):
	clienteid = models.AutoField(primary_key=True)
	clientenome = models.CharField(max_length=30)
	clienteend = models.CharField(max_length=30)
	clientefone = models.CharField(max_length=11)
	clienteemail = models.CharField(max_length=20)
	clientedoc = models.IntegerField()
	def __str__(self):
		return self.clientenome

@python_2_unicode_compatible
class produtosmad(models.Model):
	produtomadid = models.AutoField(primary_key=True)
	produtomadtipo = models.CharField(max_length=15)
	produtomaddesc = models.CharField(max_length=50)
	produtomadmedidas = models.CharField(max_length=10)
	def __str__(self):
		return self.produtomaddesc

class produtosalu(models.Model):
	produtoaluid = models.AutoField(primary_key=True)
	produtoalulinha = models.CharField(max_length=15)
	produtoaludesc = models.CharField(max_length=50)
	produtoalumedidas = models.CharField(max_length=10)
	def __str__(self):
		return self.produtoaludesc

@python_2_unicode_compatible
class obs(models.Model):
	obsid = models.AutoField(primary_key=True)
	obsdesc = models.CharField(max_length=50)
	def __str__(self):
		return self.obsdesc

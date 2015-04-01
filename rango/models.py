from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Cliente(models.Model):
	primeiro_nome = models.CharField('primeiro nome', max_length=60)
	ultimo_nome = models.CharField('ultimo nome', max_length=60, blank=True, null=True)
	telefone = models.CharField('telefone', max_length=15, blank=True, null=True)
	email = models.EmailField('email', blank=True, null=True)
	def completa_nome(self):
		return self.primeiro_nome+" "+self.ultimo_nome
	def __str__(self):
		return self.nome_completo
	nome_completo = property(completa_nome)

	

class Oservico(models.Model):
	cliente = models.ForeignKey(Cliente)
	data_abertura = models.DateTimeField(default=timezone.now)
	equipamento = models.TextField(blank= True)
	defeito = models.TextField(blank= True)
	CHOICES = (('A', 'Aberta',), ('F', 'Fechada',), ('C', 'Cancelada', ))
	situacao = models.CharField(max_length=1, choices=CHOICES, default = 'A')
	solucao = models.TextField(blank= True)
	data_fechamento = models.DateTimeField(blank=True, null=True)  ## TODO ##


	class Meta:
		verbose_name='Ordem de Serviço'
		verbose_name_plural='Ordens de Serviço'

	def __str__(self):
		return str(self.pk)

	def abrir(self):
		self.save()

	#def get_absolute_url(self):
		#return reverse('rango:editar_historico', kwargs={'pk': self.pk})


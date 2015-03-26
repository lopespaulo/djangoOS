from django import forms 
from django.forms import ModelForm
from rango.models import Cliente, Oservico
from django.utils import timezone
import datetime

#class ClienteForm(ModelForm):
	# class Meta:
	# 	model = Cliente
	# 	fields = ['primeiro_nome', 'ultimo_nome', 'telefone', 'email']

class ClienteForm(forms.ModelForm):
	primeiro_nome = forms.CharField(label='Primeiro Nome', max_length=60)
	ultimo_nome = forms.CharField(label='Ultimo nome', max_length=60)
	telefone = forms.CharField(label='telefone',max_length=15)
	email = forms.EmailField(label='e-mail')

	class Meta:
		model = Cliente
		fields = ['primeiro_nome', 'ultimo_nome', 'telefone', 'email']

#class ServicoForm(forms.Form):
#	busca = forms.CharField()

class ServicoForm(forms.ModelForm):
	class Meta:
		model = Oservico
		fields = ['id','data_abertura', 'equipamento', 'defeito',]

class EditServicoForm(forms.ModelForm):
	def clean_ServicoForm(self):
		numero_os = self.cleaned_data['id']
		return numero_os
		
	class Meta:
		model = Oservico
<<<<<<< HEAD
		fields = ['id', 'cliente', 'situacao', 'solucao','data_fechamento' ]
=======
		fields = ['numero_os', 'cliente', 'situacao', ]
>>>>>>> origin/master
	


	



def busca_usuarios():
	MY_CHOICES = (('1', 'Option 1'),('2', 'Option 2'),('3', 'Option 3'),)
	return MY_CHOICES

class MyForm(forms.Form):
	CLIENTE = forms.ChoiceField(choices=busca_usuarios())
	
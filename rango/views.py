from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from rango.forms import ClienteForm, ServicoForm, EditServicoForm
from rango.models import Oservico, Cliente
from django.core.context_processors import csrf

def index(request):
	args = {}
	args.update(csrf(request))
	args['clientes'] = Cliente.objects.all()
	return render(request, 'rango/index.html', args)

def add_cliente(request):
	#cliente = get_object_or_404(Cliente, )
	context = {}
	if request.method == 'POST':
		form = ClienteForm(request.POST)
		if form.is_valid():
			context['is_valid'] = True
			form.save()
			form = ClienteForm()
					
		else:
			print (form.errors)
	else:
		form = ClienteForm()
	context['form'] = form
	return render(request, 'rango/add_cliente.html', context)

# -- Tela de OS

def busca_cliente(request):
	if request.method == 'POST':
		search = request.POST['search_text']
	else:
		search = ' '
	clientes = Cliente.objects.filter(primeiro_nome__contains=search).exclude(primeiro_nome__contains=' ')
	return render_to_response('rango/ajax_search.html', {'clientes': clientes})	

def add_servico(request):
	#Oservico.objects.filter(cliente_id=id)
	context = {}
	if request.method == 'POST':
		form = ServicoForm(request.POST)
		if form.is_valid():
			context['is_valid'] = True
			form.save()
			form = ServicoForm()
		else:
			print (form.errors)
	else:
		form = ServicoForm()
	context['form'] = form
	return render(request, 'rango/add_os.html', context )

#Edit Form

def editar_servico(request, id):
	servico = get_object_or_404(Oservico, pk=id)
	form = EditServicoForm(request.POST or None, instance=servico)
	if form.is_valid():
		form.save()
		return redirect('rango:historico')			
	return render(request, 'rango/editar_servico.html', {'form': form} )

def historico(request):
	
	context = Oservico.objects.all()
	return render(request, 'rango/historico.html', {'context': context})




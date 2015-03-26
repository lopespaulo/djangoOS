from django.contrib import admin

from rango.models import Cliente, Oservico

class OservicoAdmin(admin.ModelAdmin):
<<<<<<< HEAD
    list_display = ( 'id', 'data_abertura', 'cliente', 'situacao')
    order_by = ('-data_abertura')
    list_filter = ('data_abertura', 'situacao', 'cliente')

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome_completo', 'telefone')
=======
	list_display = ('numero_os', 'data_abertura', 'cliente', 'situacao')
	order_by = ('-data_abertura')
	list_filter = ('data_abertura', 'situacao', 'cliente')

class ClienteAdmin(admin.ModelAdmin):
	list_display = ('nome_completo', 'telefone')
>>>>>>> origin/master



admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Oservico, OservicoAdmin)
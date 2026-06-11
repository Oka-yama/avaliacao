from django.contrib import admin
from .models import Produto

# Register your models here.
@admin.register(Produto)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('nome', 'imagem', 'preco', 'disponivel',)  
    
    list_filter = ('disponivel',) 

    search_fields = ('nome', 'descricao',)

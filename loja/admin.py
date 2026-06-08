from django.contrib import admin
from .models import Produto

# Register your models here.
@admin.register(Produto)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'preco')  
    
    list_filter = ('disponivel',) 

    search_fields = ('nome',)

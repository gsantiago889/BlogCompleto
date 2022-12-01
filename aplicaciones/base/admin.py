from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Post)
class AutorAdmin(admin.ModelAdmin):
  list_display=('titulo','slug', 'autor')
  prepopulated_fields={'slug': ('titulo',),}
  
admin.site.register(Categoria)
admin.site.register(Autor)
admin.site.register(Web)
admin.site.register(RedesSociales)
admin.site.register(Contacto)
admin.site.register(Suscriptor)

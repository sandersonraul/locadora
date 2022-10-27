from django.contrib import admin
from .models import (
  Filme,
  Cliente,
  Locacao,
  Categoria
)

admin.site.register(Filme)
admin.site.register(Cliente)
admin.site.register(Locacao)
admin.site.register(Categoria)
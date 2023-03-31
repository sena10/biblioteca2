from django.contrib import admin

from .models import Livro, Autor, Emprestimo, Perfil

admin.site.register(Livro)
admin.site.register(Autor)
admin.site.register(Emprestimo)
admin.site.register(Perfil)


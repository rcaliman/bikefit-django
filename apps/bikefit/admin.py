from django.contrib import admin
from .models import ModelCalculos, ModelMural


class AdminCalculos(admin.ModelAdmin):
    list_display = ('id', 'email', 'cavalo', 'esterno', 'braco')
    list_display_links = ('email',)
    search_field = ('email',)
    list_per_page = 10


admin.site.register(ModelCalculos, AdminCalculos)


class AdminMural(admin.ModelAdmin):
    list_display = ('data', 'nome', 'email')
    list_display_links = ('email',)
    search_field = ('email',)
    list_per_page = 10


admin.site.register(ModelMural, AdminMural)

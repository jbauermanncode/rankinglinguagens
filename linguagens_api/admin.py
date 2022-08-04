from django.contrib import admin
from linguagens_api.models import Linguagem

class Linguagens(admin.ModelAdmin):
    list_display = ('id', 'title', 'url', 'ranking')
    list_display_links = ('id','title')
    search_fields = ('title',)
    list_per_page = 10

admin.site.register(Linguagem, Linguagens)
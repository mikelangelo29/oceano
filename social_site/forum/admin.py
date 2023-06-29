from django.contrib import admin
from .models import Discussione, Sezione, Post 

class DiscussioneModelAdmin(admin.ModelAdmin):
    model = Discussione
    list_display= ["titolo", "sezione_appartenenza", "autore_discussione"]
    search_fields= ["titolo", "autore_discussione"]
    list_filter = ["sezione_appartenenza", "data_creazione"]


class PostModelAdmin (admin.ModelAdmin):
    model = Post
    list_display= ["autore_post", "discussione"]
    search_fields= ["contenuto"]
    list_filter = ["autore_post", "data_creazione"]


class SezioneModelAdmin (admin.ModelAdmin):
    model = Sezione
    list_display= ["nome_sezione", "descrizione"]
  






admin.site.register(Discussione, DiscussioneModelAdmin)
admin.site.register(Sezione, SezioneModelAdmin)
admin.site.register(Post, PostModelAdmin )

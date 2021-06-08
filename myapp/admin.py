from django.contrib import admin

from .models import Word, Visitor

class WordAdminSite(admin.ModelAdmin):
    model = Word
    fields = ['name','is_found']
    list_display = ('name','is_found')

class VisitorAdminSite(admin.ModelAdmin):
    model = Visitor
    fields = ['visitors_count','created_date']
    list_display = ('visitors_count','created_date')
# Register your models here.
admin.site.register
admin.site.register(Word,WordAdminSite)
admin.site.register(Visitor, VisitorAdminSite)
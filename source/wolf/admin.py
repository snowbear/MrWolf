from django import forms
from django.contrib import admin
from wolf import models


class SolutionAdmin(admin.ModelAdmin):
    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super(SolutionAdmin, self).formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'code':
            formfield.widget = forms.Textarea(attrs=formfield.widget.attrs)
        return formfield


class TemplateAdmin(admin.ModelAdmin):
    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super(TemplateAdmin, self).formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'code':
            formfield.widget = forms.Textarea(attrs=formfield.widget.attrs)
        return formfield

admin.site.register(models.Language)
admin.site.register(models.Template, TemplateAdmin)
admin.site.register(models.Solution, SolutionAdmin)

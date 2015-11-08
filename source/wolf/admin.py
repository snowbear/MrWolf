from django import forms
from django.contrib import admin
from wolf.models import *

class SolutionAdmin(admin.ModelAdmin):
    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super(SolutionAdmin, self).formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'code':
            formfield.widget = forms.Textarea(attrs=formfield.widget.attrs)
        return formfield

admin.site.register(Solution, SolutionAdmin)
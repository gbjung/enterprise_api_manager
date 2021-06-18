from django.contrib import admin
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.html import format_html
from django.forms import TextInput, Textarea

import nested_admin

# Register your models here.
from .models import Vertical, Section, Constraint, Parameter, Endpoint
from django.db import models

class ParameterInline(nested_admin.NestedTabularInline):
    model = Parameter
    classes = ('grp-collapse grp-closed',)
    extra=0
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows':1, 'cols':1})},
    }

class ConstraintInline(nested_admin.NestedTabularInline):
    model = Constraint
    classes = ('grp-collapse grp-closed',)
    extra=0
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows':1, 'cols':1})},
    }

class EndpointInline(nested_admin.NestedStackedInline):
    model = Endpoint
    classes = ('grp-collapse grp-open',)
    extra=0
    inlines = [ParameterInline, ConstraintInline]
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows':1, 'cols':1})},
    }

class SectionInline(nested_admin.NestedStackedInline):
    model = Section
    classes = ('grp-collapse grp-open',)
    extra=0
    inlines = [EndpointInline]
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows':1, 'cols':1})},
    }

@admin.register(Vertical)
class VerticalAdmin(nested_admin.NestedModelAdmin):
    inlines = [
        SectionInline
    ]
    list_display = ("name", "sections", "current_endpoints")

    def sections(self, obj):
        count = list(obj.sections.all().values_list('name', flat=True)) or "None"
        return count

    def current_endpoints(self, obj):
        count = sum([sect.endpoints.count() for sect in obj.sections.all()])

        return count

    sections.short_description = "Sections"

    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows':1, 'cols':0})},
    }

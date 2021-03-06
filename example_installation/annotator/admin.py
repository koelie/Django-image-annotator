from .models import *
from django.contrib import admin
from django.forms import fields, widgets

class ImageAdmin(admin.ModelAdmin):
    list_display = ('image',)


class LabelValueInline(admin.StackedInline):
    model = LabelValue
    extra = 3
    sortable_field_name = "position"
#    formfield_overrides = {
#        models.PositiveSmallIntegerField : {'widget' : widgets.HiddenInput},
#    }

class LabelAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = [LabelValueInline]

class AnnotationAdmin(admin.ModelAdmin):
    list_display = ('image', 'label', 'value')

admin.site.register(Image, ImageAdmin)
admin.site.register(Label, LabelAdmin)
admin.site.register(Annotation, AnnotationAdmin)


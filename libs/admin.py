from django.contrib import admin

from .models import *
# Register your models here.


class UrlAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'status']

    class Meta:
        model = t_url


admin.site.register(t_url, UrlAdmin)


class DictAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'status']

    class Meta:
        model = t_dict


admin.site.register(t_dict, DictAdmin)


class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject']

    class Meta:
        model = t_contact


admin.site.register(t_contact, ContactAdmin)

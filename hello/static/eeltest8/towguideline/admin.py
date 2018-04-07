from django.contrib import admin

from .models import Tow

class TowAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'slug']
    class Meta:
        model = Tow


admin.site.register(Tow, TowAdmin)

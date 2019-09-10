from django.contrib import admin

# Register your models here.
from .models import product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")

admin.site.register(product, ProductAdmin)
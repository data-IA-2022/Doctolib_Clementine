from django.contrib import admin
from application.models import FormulaireSante, FormulaireStress


class colonnes(admin.ModelAdmin):
    #list_display = ("id", "username", "role", "email","is_superuser",)  #[field.name for field in Utilisateur._meta.get_fields()]
    list_display = [field.name for field in FormulaireSante._meta.get_fields()]

admin.site.register(FormulaireSante, colonnes)

class colonnes(admin.ModelAdmin):
    #list_display = ("id", "username", "role", "email","is_superuser",)  #[field.name for field in Utilisateur._meta.get_fields()]
    list_display = [field.name for field in FormulaireStress._meta.get_fields()]

admin.site.register(FormulaireStress, colonnes)
from django.contrib import admin
from .models import Medication  # Import your model

@admin.register(Medication)  # This decorator registers the model
class MedicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'animal_type', 'mg_per_kg', 'max_dose')
    list_filter = ('animal_type',)
    search_fields = ('name', 'animal_type')
    ordering = ('name',)

# Alternative registration style (choose one):
# admin.site.register(Medication, MedicationAdmin)
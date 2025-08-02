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
    

from django.contrib import admin
from django.utils.html import format_html
from .models import Breed

@admin.register(Breed)
class BreedAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'species_display',
        'climate_display',
        'weight_display',
        'is_featured',
        'featured_status',
        'image_preview'
    )
    list_filter = ('species', 'climate_suitability', 'is_featured')
    search_fields = ('name', 'origin', 'distinguishing_features')
    list_editable = ('is_featured',)
    readonly_fields = ('date_added', 'last_updated')
    fieldsets = (
        ('Basic Information', {
            'fields': (
                'name',
                'species',
                'origin',
                'climate_suitability',
                'is_featured'
            )
        }),
        ('Physical Characteristics', {
            'fields': (
                'avg_weight_kg',
                'lifespan_years',
                'distinguishing_features'
            )
        }),
        ('Productivity', {
            'fields': (
                'milk_yield',
                'meat_quality_rating',
                'egg_production'
            )
        }),
        ('Care Requirements', {
            'fields': (
                'disease_resistance',
                'feeding_requirements',
                'special_considerations'
            )
        }),
        ('Media', {
            'fields': (
                'image',
                'video_url'
            )
        }),
        ('Metadata', {
            'fields': (
                'date_added',
                'last_updated'
            ),
            'classes': ('collapse',)
        })
    )
    
    # Custom display methods
    def species_display(self, obj):
        return obj.get_species_display()
    species_display.short_description = 'Species'
    
    def climate_display(self, obj):
        return obj.get_climate_suitability_display()
    climate_display.short_description = 'Climate'
    
    def weight_display(self, obj):
        return f"{obj.avg_weight_kg} kg"
    weight_display.short_description = 'Weight'
    
    def featured_status(self, obj):
        return "⭐" if obj.is_featured else ""
    featured_status.short_description = 'Featured'
    
    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="max-height: 50px; max-width: 50px;" />',
                obj.image.url
            )
        return "-"
    image_preview.short_description = 'Preview'
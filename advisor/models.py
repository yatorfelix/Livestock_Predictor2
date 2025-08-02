from django.db import models

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Medication(models.Model):
    name = models.CharField(max_length=100)
    animal_type = models.CharField(max_length=50)  # 'hen', 'goat', etc.
    mg_per_kg = models.DecimalField(max_digits=5, decimal_places=2)
    max_dose = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        null=True, 
        blank=True,
        help_text="Leave empty if no maximum dose"
    )
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} ({self.animal_type})"



class Breed(models.Model):
    SPECIES_CHOICES = [
        ('cattle', 'Cattle'),
        ('goat', 'Goat'),
        ('sheep', 'Sheep'),
        ('poultry', 'Poultry'),
        ('other', 'Other')
    ]
    
    CLIMATE_CHOICES = [
        ('arid', 'Arid/Hot'),
        ('temperate', 'Temperate'),
        ('cold', 'Cold'),
        ('all', 'All Climates')
    ]

    # Core Information
    name = models.CharField(max_length=100, unique=True)
    species = models.CharField(max_length=20, choices=SPECIES_CHOICES)
    origin = models.CharField(max_length=100, blank=True)
    climate_suitability = models.CharField(max_length=20, choices=CLIMATE_CHOICES)
    
    # Physical Characteristics
    avg_weight_kg = models.PositiveIntegerField(help_text="Average weight in kilograms")
    lifespan_years = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(30)],
        help_text="Typical lifespan in years"
    )
    distinguishing_features = models.TextField(blank=True)
    
    # Productivity Metrics
    milk_yield = models.CharField(
        max_length=50,
        blank=True,
        help_text="e.g., 5-8L/day for dairy breeds"
    )
    meat_quality_rating = models.PositiveIntegerField(
        blank=True,
        null=True,
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        help_text="Rating 1-5 (5=best)"
    )
    egg_production = models.CharField(
        max_length=50,
        blank=True,
        help_text="e.g., 100-120/year for poultry"
    )
    
    # Care Requirements
    disease_resistance = models.TextField(blank=True)
    feeding_requirements = models.TextField(blank=True)
    special_considerations = models.TextField(blank=True)
    
    # Media
    image = models.ImageField(
        upload_to='advisor/images/breeds/',
        blank=True,
        help_text="Optimal size: 600x400px"
    )
    video_url = models.URLField(
        blank=True,
        help_text="YouTube/Vimeo link (optional)"
    )
    
    # Metadata
    date_added = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    is_featured = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.name} ({self.get_species_display()})"
    
    class Meta:
        ordering = ['species', 'name']
        verbose_name_plural = "Breeds"
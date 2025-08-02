from django.db import models

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
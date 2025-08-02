def calculate_dosage(animal_weight, medication):
    """Calculate dosage and return formatted recommendations"""
    dosage = float(animal_weight) * float(medication.mg_per_kg)
    
    if medication.max_dose and dosage > medication.max_dose:
        return {
            'calculated': dosage,
            'recommended': medication.max_dose,
            'warning': f"Maximum safe dose exceeded ({medication.max_dose}mg max)",
            'notes': medication.notes
        }
    
    return {
        'calculated': dosage,
        'recommended': dosage,
        'warning': None,
        'notes': medication.notes
    }
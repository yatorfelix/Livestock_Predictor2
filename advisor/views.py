from django.shortcuts import render, redirect
from datetime import datetime
import random
from django.shortcuts import render
from .models import Medication
from .calculators import calculate_dosage

import requests
from django.shortcuts import render
from django.core.cache import cache
from django.http import JsonResponse


import requests
from django.shortcuts import render
from django.core.cache import cache  # For caching API responses




from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Breed



def home(request):
    animals = [
        {'name': 'Hen', 'slug': 'hen', 'image': 'images/hen.jpg'},
        {'name': 'Goat', 'slug': 'goat', 'image': 'images/goat.jpg'},
        {'name': 'Cow', 'slug': 'cow', 'image': 'images/cow.jpg'},
        {'name': 'Sheep', 'slug': 'sheep', 'image': 'images/sheep.jpg'},
    ]
    return render(request, 'advisor/home.html', {'animals': animals})

def diagnosis(request, animal_type):
    symptoms_lists = {
        'hen': [
            'lethargy', 'diarrhea', 'green droppings', 'sneezing', 'nasal discharge',
            'swollen face', 'twisting of neck', 'loss of appetite', 'scabs on comb',
            'difficulty breathing', 'bloody diarrhea', 'dehydration', 'drop in egg production',
            'soft-shelled eggs', 'weight loss', 'pale comb', 'swollen joints', 'lameness',
            'purple comb', 'eye swelling', 'open-mouth breathing', 'unsteady walking', 'head tilt'
        ],
        'goat': [
            'coughing', 'weight loss', 'diarrhea', 'rough coat', 'poor appetite',
            'labored breathing', 'scabs on lips', 'sore mouth', 'swollen jaw',
            'pale gums', 'bloating', 'nasal discharge'
        ],
        'cow': [
            'fever', 'milk drop', 'swollen udder', 'bloated abdomen', 'no rumination',
            'blood in urine', 'high fever', 'tick infestation', 'swollen lymph nodes',
            'respiratory distress', 'nasal discharge', 'coughing', 'depression',
            'watery diarrhea', 'dehydration', 'abortion', 'retained placenta',
            'muscle tremors', 'aggression', 'hypersalivation', 'lameness', 'swollen joints',
            'yellow eyes', 'dark red urine', 'sudden death', 'bloody discharge'
        ],
        'sheep': [
            'wool loss', 'scabs or sores', 'weight loss', 'nasal discharge', 'lameness',
            'coughing', 'diarrhea', 'fever', 'swollen joints', 'depression', 'rough coat',
            'labored breathing'
        ]
    }

    if request.method == 'POST':
        symptoms = request.POST.getlist('symptoms')
        diagnosis_data = diagnose_animal(animal_type, symptoms)
        
        # Store in session for report generation
        request.session['diagnosis_data'] = diagnosis_data
        request.session['animal_type'] = animal_type
        request.session['symptoms'] = symptoms
        
        return redirect('diagnosis_report', animal_type=animal_type)

    context = {
        'animal': animal_type,
        'hen_symptoms': symptoms_lists.get('hen', []),
        'goat_symptoms': symptoms_lists.get('goat', []),
        'cow_symptoms': symptoms_lists.get('cow', []),
        'sheep_symptoms': symptoms_lists.get('sheep', [])
    }
    return render(request, 'advisor/diagnosis.html', context)

def diagnose_animal(animal_type, symptoms):
    # Base template for all results
    base_result = {
        'diagnosis': 'Unknown condition - please consult veterinarian',
        'severity': 'medium',
        'confidence': random.randint(40, 70),
        'treatment': '''
        1. Isolate animal immediately
        2. Provide supportive care (hydration, nutrition)
        3. Monitor vital signs twice daily
        4. Consult veterinarian within 24 hours
        ''',
        'prevention': [
            "Maintain proper hygiene standards",
            "Ensure vaccination schedule is current",
            "Implement biosecurity measures",
            "Schedule regular health checkups"
        ]
    }

    # Hen Diagnosis Logic
    if animal_type == 'hen':
        if all(symptom in symptoms for symptom in ['lethargy', 'diarrhea', 'green droppings']):
            return {
                **base_result,
                'diagnosis': 'Newcastle Disease (Highly contagious viral disease)',
                'severity': 'high',
                'confidence': 90,
                'treatment': '''
                1. Administer Newcastle vaccine booster (0.5ml intramuscular)
                2. Isolate for 21 days minimum
                3. Add electrolytes to drinking water
                4. Disinfect housing with virkon solution
                ''',
                'prevention': base_result['prevention'] + [
                    "Vaccinate chicks at day 1 and week 4",
                    "Control wild bird access to coop"
                ]
            }
        elif 'sneezing' in symptoms and 'nasal discharge' in symptoms:
            return {
                **base_result,
                'diagnosis': 'Infectious Coryza (Bacterial respiratory infection)',
                'severity': 'medium',
                'confidence': 80,
                'treatment': '''
                1. Administer erythromycin (20mg/kg for 5 days)
                2. Improve ventilation in coop
                3. Provide vitamin supplements
                '''
            }

    # Goat Diagnosis Logic
    elif animal_type == 'goat':
        if 'bloating' in symptoms and 'discomfort' in symptoms:
            return {
                **base_result,
                'diagnosis': "Bloat (Rumen gas accumulation)",
                'severity': 'high',
                'confidence': 95,
                'treatment': '''
                1. Administer poloxalene (follow label instructions)
                2. Walk goat gently for 15 minutes
                3. Use stomach tube to relieve gas if trained
                '''
            }

    # Cow Diagnosis Logic
    elif animal_type == 'cow':
        if 'fever' in symptoms and 'milk drop' in symptoms:
            return {
                **base_result,
                'diagnosis': "Mastitis (Udder infection)",
                'severity': 'medium',
                'confidence': 85,
                'treatment': '''
                1. Administer intramammary antibiotics
                2. Apply warm compresses 3x daily
                3. Milk out affected quarter every 2 hours
                '''
            }

    # Sheep Diagnosis Logic
    elif animal_type == 'sheep':
        if 'wool loss' in symptoms and 'itching' in symptoms:
            return {
                **base_result,
                'diagnosis': "Sheep Scab (Mite infestation)",
                'severity': 'medium',
                'confidence': 75,
                'treatment': '''
                1. Apply ivermectin injection (0.2mg/kg)
                2. Repeat in 10-14 days
                3. Isolate for 6 weeks minimum
                '''
            }

    # Fallback for unmatched cases
    matched_symptoms = len(symptoms)
    if matched_symptoms > 3:
        base_result.update({
            'diagnosis': 'Potential multiple conditions - urgent vet consultation needed',
            'severity': 'high',
            'confidence': 60
        })
    elif matched_symptoms > 0:
        base_result.update({
            'diagnosis': 'Mild condition - monitor closely',
            'severity': 'low',
            'confidence': 40
        })

    return base_result

def diagnosis_report(request, animal_type):
    # Retrieve data from session
    diagnosis_data = request.session.get('diagnosis_data', {})
    symptoms = request.session.get('symptoms', [])
    
    context = {
        'animal': animal_type,
        'report_date': datetime.now().strftime("%B %d, %Y %H:%M"),
        'case_id': f"{random.randint(1000, 9999)}-{datetime.now().year}",
        'symptoms': symptoms,
        'diagnosis': diagnosis_data.get('diagnosis', 'No diagnosis available'),
        'severity': diagnosis_data.get('severity', 'medium'),
        'confidence': diagnosis_data.get('confidence', 50),
        'treatment': diagnosis_data.get('treatment', 'Please consult a veterinarian'),
        'prevention': diagnosis_data.get('prevention', [])
    }
    
    return render(request, 'advisor/report.html', context)

# Other views remain unchanged
def result(request):
    return render(request, 'advisor/result.html')

def about(request):
    return render(request, 'advisor/about.html')

def resources(request):
    return render(request, 'advisor/resources.html')

def contact(request):
    return render(request, 'advisor/contact.html')



def medication_calculator(request):
    medications = Medication.objects.all()
    result = None
    
    if request.method == 'POST':
        medication_id = request.POST.get('medication')
        animal_weight = request.POST.get('weight')
        
        try:
            medication = Medication.objects.get(id=medication_id)
            result = calculate_dosage(animal_weight, medication)
        except (Medication.DoesNotExist, ValueError) as e:
            result = {'error': str(e)}
    
    return render(request, 'advisor/calculator.html', {
        'medications': medications,
        'result': result
    })

def weather_advice(request):
    # Default coordinates (Nairobi)
    lat = request.GET.get('lat', '-1.286389')
    lon = request.GET.get('lon', '36.817223')
    api_key = "86d7587d665e97d94e23620b3f977c01"
    
    cache_key = f"weather_{lat}_{lon}"
    weather_data = cache.get(cache_key)
    advice = []

    if not weather_data:
        try:
            # 1. Make API request with timeout
            url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"
            response = requests.get(url, timeout=10).json()
            
            # 2. Validate API response
            if not isinstance(response, dict):
                raise ValueError("Invalid API response format")
            
            if 'main' not in response:
                raise KeyError("'main' field missing in response")
                
            if 'weather' not in response or not response['weather']:
                raise KeyError("Weather conditions data missing")

            # 3. Extract data with fallbacks
            weather_data = {
                "temp": round(response["main"].get("temp", 0) - 273.15, 1),  # Default 0°C if missing
                "humidity": response["main"].get("humidity", 50),  # Default 50%
                "rain": response.get("rain", {}).get("1h", 0),
                "conditions": response["weather"][0].get("main", "clear").lower(),
                "location": response.get("name", "Unknown Location"),  # City name
                "country": response.get("sys", {}).get("country", ""),  # Country code
                "success": True
            }
            cache.set(cache_key, weather_data, 1800)

        except Exception as e:
            weather_data = {
                "error": f"Failed to get weather data: {str(e)}",
                "success": False
            }

    # Generate advice only if we have valid data
    if weather_data.get("success"):
        if weather_data["humidity"] > 80:
            advice.append("⚠️ High humidity → Risk of fungal infections. Apply antifungal sprays.")
        if weather_data["temp"] > 35:
            advice.append("🔥 Extreme heat → Provide shade and extra water for livestock.")
        if weather_data["rain"] > 5:
            advice.append("🌧️ Heavy rain → Move animals to dry areas to prevent foot rot.")

    context = {
        "weather": weather_data,
        "advice": advice if advice else ["No weather-related risks detected."]
    }
    
    # Return JSON for AJAX requests
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest' or request.GET.get('format') == 'json':
        return JsonResponse(context)
    
    # Return HTML for direct access
    return render(request, "advisor/weather_advice.html", context)



class BreedListView(ListView):
    model = Breed
    template_name = 'advisor/breeds.html'
    context_object_name = 'breeds'
    paginate_by = 12
    
    def get_queryset(self):
        queryset = super().get_queryset()
        
        # Filter by species
        species = self.request.GET.get('species')
        if species:
            queryset = queryset.filter(species=species)
        
        # Filter by climate
        climate = self.request.GET.get('climate')
        if climate:
            queryset = queryset.filter(climate_suitability=climate)
        
        # Filter featured
        featured = self.request.GET.get('featured')
        if featured == '1':
            queryset = queryset.filter(is_featured=True)
        
        return queryset.order_by('species', 'name')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['species_choices'] = dict(Breed.SPECIES_CHOICES)
        context['climate_choices'] = dict(Breed.CLIMATE_CHOICES)
        return context

class BreedDetailView(DetailView):
    model = Breed
    template_name = 'advisor/breed_detail.html'
    context_object_name = 'breed'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related_breeds'] = Breed.objects.filter(
            species=self.object.species
        ).exclude(
            pk=self.object.pk
        )[:4]
        return context
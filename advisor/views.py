from django.shortcuts import render

def home(request):
    animals = [
        {'name': 'Hen', 'slug': 'hen', 'image': 'images/hen.jpg'},
        {'name': 'Goat', 'slug': 'goat', 'image': 'images/goat.jpg'},
        {'name': 'Cow', 'slug': 'cow', 'image': 'images/cow.jpg'},
        {'name': 'Sheep', 'slug': 'sheep', 'image': 'images/sheep.jpg'},
    ]
    return render(request, 'advisor/home.html', {'animals': animals})

def diagnosis(request, animal_type):
    diagnosis_result = None

    if request.method == 'POST':
        symptoms = request.POST.getlist('symptoms')

        if animal_type == 'hen':
            if 'lethargy' in symptoms and 'diarrhea' in symptoms and 'green droppings' in symptoms:
                diagnosis_result = 'Possibly Newcastle Disease – a viral disease that spreads quickly and causes respiratory and neurological signs.'
            elif 'sneezing' in symptoms and 'nasal discharge' in symptoms and 'swollen face' in symptoms:
                diagnosis_result = 'Possibly Infectious Coryza – a bacterial disease characterized by respiratory symptoms and facial swelling.'
            elif 'twisting of neck' in symptoms and 'loss of appetite' in symptoms:
                diagnosis_result = 'Possibly Marek\'s Disease – a viral disease that affects nerves and causes paralysis and tumors.'
            elif 'scabs on comb' in symptoms and 'difficulty breathing' in symptoms:
                diagnosis_result = 'Possibly Fowl Pox – a viral disease causing skin lesions and respiratory issues.'
            elif 'bloody diarrhea' in symptoms and 'dehydration' in symptoms:
                diagnosis_result = 'Possibly Coccidiosis – a parasitic disease causing intestinal damage and bloody stool.'
            elif 'drop in egg production' in symptoms and 'soft-shelled eggs' in symptoms:
                diagnosis_result = 'Possibly Egg Drop Syndrome – a viral condition affecting egg quality and quantity.'
            elif 'ruffled feathers' in symptoms and 'weight loss' in symptoms and 'pale comb' in symptoms:
                diagnosis_result = 'Possibly Worm Infestation – internal parasites causing poor health and appearance.'
            elif 'swollen joints' in symptoms and 'lameness' in symptoms:
                diagnosis_result = 'Possibly Mycoplasma synoviae – a bacterial infection affecting joints and movement.'
            elif 'sudden death' in symptoms and 'purple comb' in symptoms:
                diagnosis_result = 'Possibly Avian Influenza – a severe viral disease with high mortality.'
            elif 'nasal discharge' in symptoms and 'eye swelling' in symptoms and 'open-mouth breathing' in symptoms:
                diagnosis_result = 'Possibly Infectious Bronchitis – a contagious respiratory virus.'
            elif 'unsteady walking' in symptoms and 'head tilt' in symptoms:
                diagnosis_result = 'Possibly Encephalomalacia – a vitamin E deficiency leading to nervous disorders.'
            else:
                diagnosis_result = 'Symptoms do not match a specific disease. Further examination or lab tests are recommended.'



        elif animal_type == 'goat':
            if 'coughing' in symptoms and 'weight loss' in symptoms and 'labored breathing' in symptoms:
                diagnosis_result = 'Possibly Pneumonia – a respiratory disease in goats caused by bacteria or viruses.'
            elif 'diarrhea' in symptoms and 'poor appetite' in symptoms:
                diagnosis_result = 'Possibly Coccidiosis – a parasitic infection, common in young goats.'
            elif 'sore mouth' in symptoms and 'scabs on lips' in symptoms:
                diagnosis_result = 'Possibly Orf (Contagious Ecthyma) – a viral skin disease common in kids.'
            elif 'bloating' in symptoms and 'discomfort' in symptoms:
                diagnosis_result = 'Possibly Bloat – excessive gas in the rumen, often fatal if untreated.'
            elif 'limping' in symptoms and 'swollen joints' in symptoms:
                diagnosis_result = 'Possibly Joint Ill (Arthritis) – usually caused by bacterial infection in kids.'
            elif 'anemia' in symptoms and 'pale gums' in symptoms:
                diagnosis_result = 'Possibly Barber Pole Worm (Haemonchosis) – a dangerous blood-sucking parasite.'
            elif 'nasal discharge' in symptoms and 'sneezing' in symptoms:
                diagnosis_result = 'Possibly Caprine Nasal Rhinitis – inflammation of the nasal passages.'
            elif 'abortion' in symptoms and 'fever' in symptoms:
                diagnosis_result = 'Possibly Brucellosis – a bacterial infection causing reproductive failure.'
            elif 'itching' in symptoms and 'hair loss' in symptoms:
                diagnosis_result = 'Possibly Mites or Lice Infestation – causes irritation, scratching, and skin damage.'
            elif 'stiffness' in symptoms and 'muscle tremors' in symptoms:
                diagnosis_result = 'Possibly Tetanus – caused by *Clostridium tetani*, often fatal if not vaccinated.'
            elif 'weakness' in symptoms and 'difficulty standing' in symptoms:
                diagnosis_result = 'Possibly White Muscle Disease – caused by selenium and vitamin E deficiency.'
            elif 'frequent urination' in symptoms and 'straining' in symptoms:
                diagnosis_result = 'Possibly Urinary Calculi – mineral buildup that blocks the urinary tract, especially in males.'
            elif 'sudden death' in symptoms and 'bloating' in symptoms and 'high fever' in symptoms:
                diagnosis_result = 'Possibly Enterotoxemia (Pulpy Kidney Disease) – caused by Clostridium perfringens.'
            else:
                diagnosis_result = 'Possibly Internal Parasites (Worms) – common in goats, especially in wet seasons, leading to anemia, weight loss, and poor coat condition.'

        elif animal_type == 'cow':
            if 'fever' in symptoms and 'milk drop' in symptoms and 'swollen udder' in symptoms:
                diagnosis_result = 'Possibly Mastitis – an inflammation of the udder, usually due to infection.'
            elif 'bloated abdomen' in symptoms and 'no rumination' in symptoms:
                diagnosis_result = 'Possibly Bloat – a digestive disorder that can be fatal if untreated.'
            elif 'blood in urine' in symptoms and 'high fever' in symptoms:
                diagnosis_result = 'Possibly Red Water Disease – a parasitic disease caused by Babesia.'
            elif 'tick infestation' in symptoms and 'swollen lymph nodes' in symptoms and 'respiratory distress' in symptoms:
                diagnosis_result = 'Possibly East Coast Fever – a deadly tick-borne disease causing fever and respiratory issues.'
            elif 'nasal discharge' in symptoms and 'coughing' in symptoms and 'depression' in symptoms:
                diagnosis_result = 'Possibly Contagious Bovine Pleuropneumonia – a serious respiratory infection.'
            elif 'watery diarrhea' in symptoms and 'dehydration' in symptoms:
                diagnosis_result = 'Possibly E. coli Infection – often seen in calves, causing severe diarrhea.'
            elif 'abortion' in symptoms and 'retained placenta' in symptoms:
                diagnosis_result = 'Possibly Brucellosis – a bacterial disease affecting reproduction.'
            elif 'muscle tremors' in symptoms and 'aggression' in symptoms and 'hypersalivation' in symptoms:
                diagnosis_result = 'Possibly Rabies – a fatal viral disease transmitted through bites.'
            elif 'lameness' in symptoms and 'swollen joints' in symptoms:
                diagnosis_result = 'Possibly Foot-and-Mouth Disease – a highly contagious viral disease causing blisters and fever.'
            elif 'yellow eyes' in symptoms and 'dark red urine' in symptoms:
                diagnosis_result = 'Possibly Leptospirosis – a bacterial disease affecting the liver and kidneys.'
            elif 'sudden death' in symptoms and 'bloody discharge' in symptoms:
                diagnosis_result = 'Possibly Anthrax – a deadly bacterial disease with rapid onset.'
            else:
                diagnosis_result = 'Possibly Internal Parasites or General Infection – monitor symptoms and consult a vet.'

        elif animal_type == 'sheep':
            if 'lameness' in symptoms and 'swollen hoof' in symptoms and 'bad odor' in symptoms:
                diagnosis_result = 'Possibly Foot Rot – a bacterial infection of the hooves common in wet conditions.'
            elif 'nasal discharge' in symptoms and 'coughing' in symptoms:
                diagnosis_result = 'Possibly Pasteurellosis – a respiratory bacterial disease.'
            elif 'itching' in symptoms and 'wool loss' in symptoms:
                diagnosis_result = 'Possibly Sheep Scab – caused by mites, leads to intense itching and wool loss.'
            elif 'diarrhea' in symptoms and 'anemia' in symptoms and 'weight loss' in symptoms:
                diagnosis_result = 'Possibly Helminthiasis (Worm Infestation) – a common internal parasitic disease that reduces productivity.'
            elif 'swollen lymph nodes' in symptoms and 'abscesses' in symptoms:
                diagnosis_result = 'Possibly Caseous Lymphadenitis – a chronic bacterial disease causing internal and external abscesses.'
            elif 'fever' in symptoms and 'abortions' in symptoms:
                diagnosis_result = 'Possibly Brucellosis – a bacterial infection that may cause abortions in pregnant sheep.'
            elif 'nasal discharge' in symptoms and 'eye discharge' in symptoms:
                diagnosis_result = 'Possibly Ovine Progressive Pneumonia (OPP) – a viral disease affecting lungs and weight gain.'
            elif 'depression' in symptoms and 'poor appetite' in symptoms:
                diagnosis_result = 'Possibly Enterotoxemia – often caused by overeating or sudden dietary changes.'
            else:
                diagnosis_result = 'Possibly Nutritional Deficiency or Generalized Infection – please consult a veterinarian for detailed diagnosis.'

    return render(request, 'advisor/diagnosis.html', {
        'animal': animal_type,
        'diagnosis': diagnosis_result
    })

def result(request):
    return render(request, 'advisor/result.html')

def about(request):
    return render(request, 'advisor/about.html')

def resources(request):
    return render(request, 'advisor/resources.html')

def contact(request):
    return render(request, 'advisor/contact.html')

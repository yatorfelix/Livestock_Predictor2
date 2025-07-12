from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def home(request):
    return render(request,'advisor/home.html')

def diagnosis(request):
    if request.method == 'POST':
        request.session['fever'] = request.POST.get('fever') == 'yes'
        request.session['drooling'] = request.POST.get('drooling') == 'yes'
        request.session['mouth_blisters'] = request.POST.get('mouth_blisters') == 'yes'
        request.session['limping'] = request.POST.get('limping') == 'yes'
        request.session['high_fever'] = request.POST.get('high_fever') == 'yes'
        request.session['swollen_lymph'] = request.POST.get('swollen_lymph') == 'yes'
        request.session['breathing_difficulty'] = request.POST.get('breathing_difficulty') == 'yes'
        request.session['udder_swelling'] = request.POST.get('udder_swelling') == 'yes'
        request.session['hot_udder'] = request.POST.get('hot_udder') == 'yes'
        request.session['bad_milk'] = request.POST.get('bad_milk') == 'yes'
        request.session['weight_loss'] = request.POST.get('weight_loss') == 'yes'
        request.session['dull_coat'] = request.POST.get('dull_coat') == 'yes'
        request.session['diarrhea'] = request.POST.get('diarrhea') == 'yes'
        request.session['sudden_death'] = request.POST.get('sudden_death') == 'yes'
        request.session['bleeding'] = request.POST.get('bleeding') == 'yes'
        request.session['stiffness'] = request.POST.get('stiffness') == 'yes'
        return redirect('result')  # Redirect only on POST
    return render(request, 'advisor/diagnosis.html')  # Show form on GET


def result(request):
    # Retrieve symptoms from session
    fever = request.session.get('fever', False)
    drooling = request.session.get('drooling', False)
    mouth_blisters = request.session.get('mouth_blisters', False)
    limping = request.session.get('limping', False)
    high_fever = request.session.get('high_fever', False)
    swollen_lymph = request.session.get('swollen_lymph', False)
    breathing_difficulty = request.session.get('breathing_difficulty', False)
    udder_swelling = request.session.get('udder_swelling', False)
    hot_udder = request.session.get('hot_udder', False)
    bad_milk = request.session.get('bad_milk', False)
    weight_loss = request.session.get('weight_loss', False)
    dull_coat = request.session.get('dull_coat', False)
    diarrhea = request.session.get('diarrhea', False)
    sudden_death = request.session.get('sudden_death', False)
    bleeding = request.session.get('bleeding', False)
    stiffness = request.session.get('stiffness', False)

    diagnosis = "No clear diagnosis based on symptoms provided."
    advice = "Please consult a veterinarian."

    # Rule 1: Foot and Mouth Disease
    if fever and drooling and mouth_blisters and limping:
        diagnosis = "Foot and Mouth Disease"
        advice = "Isolate the animal and consult a veterinarian immediately."

    # Rule 2: East Coast Fever
    elif high_fever and swollen_lymph and breathing_difficulty:
        diagnosis = "East Coast Fever"
        advice = "Treat with anti-protozoal drugs and consult a vet."

    # Rule 3: Mastitis
    elif udder_swelling and hot_udder and bad_milk:
        diagnosis = "Mastitis"
        advice = "Clean the udder and administer prescribed antibiotics."

    # Rule 4: Worm Infestation
    elif weight_loss and dull_coat and diarrhea:
        diagnosis = "Worm Infestation"
        advice = "Administer appropriate deworming medication."

    # Rule 5: Anthrax
    elif sudden_death and bleeding and stiffness:
        diagnosis = "Anthrax"
        advice = "Report to animal health authorities immediately. Avoid contact."

    return render(request, 'advisor/result.html', {
        'diagnosis': diagnosis,
        'advice': advice
    })
def about(request):
    return render(request, 'advisor/about.html')

def resources(request):
    return render(request, 'advisor/resources.html')


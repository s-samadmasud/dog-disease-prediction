from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import joblib

app = Flask(__name__)

# Load model and encoders
model = joblib.load('models/best_model.pkl')
le = joblib.load('models/label_encoder.pkl')

# Load datasets
description = pd.read_csv('datasets/description.csv')
precautions = pd.read_csv('datasets/precautions.csv')
medications = pd.read_csv('datasets/medications.csv')
diets = pd.read_csv('datasets/diets.csv')
workout = pd.read_csv('datasets/workout.csv')

# Symptoms
symptoms = [
    'difficulty_breathing', 'lethargy', 'loss_of_appetite', 'hair_loss', 'pallor', 'limping', 'muscle_loss', 'unable_to_jump',
    'lumps_or_bumps', 'weight_loss', 'swelling', 'discharge_below_eye', 'cloudy_pupils', 'impaired_vision', 'red_thick_bump',
    'persistent_diarrhea', 'exercise_intolerance', 'coughing', 'heart_murmur', 'skin_flakes', 'difficulty_walking', 'trembling_hind_legs',
    'persistent_itching', 'scabbing', 'hearing_loss', 'inflammation_ear', 'brown_particles_ear', 'fever', 'sores', 'nose_bleeds', 'pale_gums',
    'favoring_one_leg', 'ulceration', 'severe_itching', 'rash', 'bloat', 'empty_retches', 'swollen_midsection', 'bleeding', 'pain', 'redness_inflammation',
    'vision_loss', 'cloudiness_in_cornea', 'sensitivity_to_light', 'excessive_thirst', 'urination_changes', 'seizures', 'behavioral_changes', 'vomiting'
]

symptoms_dict = {symptom: idx for idx, symptom in enumerate(symptoms)}

def format_disease_name(name):
    return name.replace('_', ' ').title()

def helper(dis):
    desc = description[description['Disease'] == dis]['Description']
    desc = " ".join([w for w in desc])

    pre = precautions[precautions['Disease'] == dis][['Precaution_1', 'Precaution_2', 'Precaution_3', 'Precaution_4']]
    pre = [col for col in pre.values]

    med = medications[medications['Disease'] == dis]['Medication']
    med = [med for med in med.values]

    die = diets[diets['Disease'] == dis]['Diet']
    die = [die for die in die.values]

    wrkout = workout[workout['disease'] == dis]['workout']
    wrkout = [w for w in wrkout.values]

    return desc, pre, med, die, wrkout

def get_predicted_value(patient_symptoms):
    input_vector = np.zeros(len(symptoms_dict))
    for item in patient_symptoms:
        if item in symptoms_dict:
            input_vector[symptoms_dict[item]] = 1
    input_vector = pd.DataFrame([input_vector], columns=symptoms_dict.keys())
    pred_encoded = model.predict(input_vector)[0]
    pred_label = le.inverse_transform([pred_encoded])[0]
    return pred_label

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        selected_symptoms = request.form.getlist('symptoms')

        if not selected_symptoms:
            return render_template('index.html', symptoms=symptoms, message="Please select at least one symptom.")

        predicted_disease = get_predicted_value(selected_symptoms)
        formatted_disease = format_disease_name(predicted_disease)

        desc, pre, med, die, wrkout = helper(formatted_disease)

        return render_template('index.html', symptoms=symptoms,
                               predicted_disease=formatted_disease,
                               dis_des=desc,
                               my_precautions=pre[0],
                               medications=med,
                               my_diet=die,
                               workout=wrkout)

    return render_template('index.html', symptoms=symptoms)
@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)

import pandas as pd

# Your completed disease_symptoms dictionary
disease_symptoms = {
    'asthma': ['difficulty_breathing', 'blue_or_purple_tinge_to_tongue_or_gums', 'lethargy', 'loss_of_appetite'],
    'alopecia': ['hair_loss_and_bald_patches', 'scaly_inflamed_or_discolored_skin', 'scratching_or_chewing', 'lethargy'],
    'anemia': ['pallor_in_gums_tongue_and_ear', 'lethargy'],
    'arthritis': ['limping', 'muscle_loss', 'difficulty_sitting', 'lethargy', 'less_playful', 'grouchiness', 'unable_to_jump_up'],
    'cancer': ['lumps_or_bumps_under_the_skin', 'changes_in_eating_habits', 'increased_urination_or_drinking', 'difficulty_exercising',
               'weight_loss', 'depression', 'discharge_and_sores', 'difficulty_urinating'],
    'carnassial_tooth_abscess': ['swelling', 'discharge_below_eye', 'fever', 'loss_of_appetite', 'depression'],
    'cataracts': ['cloudy_or_cracked_pupils', 'eye_redness_swelling_inflammation', 'impaired_vision', 'dizziness', 'vomiting', 'pacing', 'restlessness', 'less_movement'],
    'cherry_eye': ['red_thick_irritated_bump_in_corner_of_eye', 'rubbing_or_scratching_eye'],
    'coccidia': ['diarrhea_with_mucus_or_blood', 'persistent_diarrhea'],
    'congestive_heart_failure': ['exercise_intolerance', 'excessive_panting', 'coughing', 'heart_murmur'],
    'dandruff': ['skin_flakes', 'dry_irritated_skin', 'excessive_scratching_biting_licking'],
    'degenerative_myelopathy': ['difficulty_getting_up', 'difficulty_walking', 'clumsiness', 'trembling_hind_legs',
                                'difficulty_breathing', 'incontinence', 'organ_failure', 'muscle_atrophy'],
    'demodectic_mange': ['persistent_itching', 'hair_loss', 'bald_spots', 'scabbing', 'sores', 'lesions', 'redness', 'scaling'],
    'ear_infection': ['hearing_loss', 'inflammation_redness_ear_canal', 'milky_odorous_discharge', 'nystagmus', 'ear_dragging', 'head_shaking'],
    'ear_mites': ['brown_particles_in_ear', 'ear_swelling', 'head_shaking', 'ear_scratching', 'ear_odor'],
    'ehrlichiosis': ['fever', 'sores', 'inflammation_of_blood_vessels', 'nose_bleeds', 'pale_gums', 'swollen_lymph_nodes',
                     'breathing_problems', 'coughing', 'increased_urination', 'eye_problems', 'lameness', 'confusion', 'disorientation', 'behavior_changes'],
    'elbow_dysplasia': ['limping_or_lameness', 'favoring_one_leg', 'abnormal_gait', 'elbow_swelling', 'lethargy', 'pain'],
    'fibrosarcoma': ['lump', 'ulceration_bleeding', 'swelling_affected_area', 'loss_of_appetite', 'loss_of_sociability', 'pain'],
    'flea_allergy_dermatitis': ['severe_itching', 'skin_redness', 'pus_filled_bumps', 'hair_loss', 'rash', 'recurrent_tapeworm'],
    'gastric_torsion': ['bloat', 'empty_retches', 'swollen_midsection', 'increased_saliva', 'difficulty_breathing',
                        'fatigue', 'rapid_heartbeat', 'pale_gums', 'drop_in_body_temperature', 'restlessness', 'anxiety', 'shock'],
    'gingivitis': ['bleeding', 'gum_redness', 'swollen_gums', 'bad_breath'],
    'glaucoma': ['pain', 'redness_inflammation', 'dilated_pupils', 'light_sensitivity', 'eye_discharge', 'vision_loss', 'cloudy_cornea', 'eye_enlargement', 'behavioral_changes'],
    'heartworm': ['cough', 'fatigue', 'trouble_breathing', 'reluctance_to_exercise', 'abnormal_lung_sounds'],
    'hemangiosarcoma': ['exhaustion', 'depression', 'loss_of_appetite', 'anemia'],
    'high_blood_pressure': ['rapid_heart_rate', 'dilated_pupils', 'nosebleeds', 'blood_in_urine', 'difficulty_seeing',
                            'enlarged_thyroid_gland', 'misshapen_kidneys'],
    'hip_dysplasia': ['avoiding_activities', 'difficulty_getting_up', 'difficulty_jumping', 'lameness'],
    'hookworm': ['anemia', 'bloody_or_black_stool', 'diarrhea', 'pruritus', 'dermatitis_paw_pads'],
    'hot_spots': ['sensitivity', 'circular_red_swollen_patches', 'pus_or_discharge', 'unpleasant_odor',
                  'hair_loss', 'excessive_licking_biting_scratching', 'fear_or_aggression'],
    'hyperthyroidism': ['weight_loss', 'increased_appetite', 'excessive_shedding', 'vomiting', 'diarrhea',
                        'hyperactivity', 'enlarged_thyroid_gland', 'trouble_breathing', 'increased_thirst_urination'],
    'hypothyroidism': ['thinning_fur', 'dull_coat', 'excessive_shedding', 'thickened_skin', 'darkened_skin',
                       'weight_gain_with_decreased_appetite', 'lethargy', 'exercise_intolerance', 'cold_intolerance'],
    'kennel_cough': ['dry_hacking_cough', 'honking_sound', 'retching_white_foamy_discharge', 'snorting', 'nasal_discharge', 'sneezing', 'pink_eye'],
    'keratoconjunctivitis_sicca': ['dull_eyes', 'eye_discharge', 'redness_eyelid', 'light_sensitivity', 'eye_scratching', 'cornea_changes', 'vision_loss', 'frantic_behavior'],
    'liver_disease': ['loss_of_appetite', 'weight_loss', 'weakness_or_lack_of_energy', 'depression', 'vomiting_and_stomach_pain', 'increased_thirst_urination', 'jaundice'],
    'liver_shunt': ['stunted_growth', 'slow_weight_gain', 'poor_muscle_development', 'seizures', 'drooling',
                    'vomiting', 'diarrhea', 'head_pressing', 'disorientation', 'depression', 'shaking', 'kidney_bladder_infections', 'kidney_stones'],
    'lyme_disease': ['depression', 'fever', 'lameness', 'loss_of_appetite', 'presence_of_ticks'],
    'nuclear_sclerosis': ['blue_gray_lens', 'minor_vision_decrease'],
    'otitis_externa': ['ear_scratching', 'head_shaking_or_tilting', 'strong_ear_odor', 'ear_pain', 'red_thick_ear', 'reluctance_to_open_mouth', 'cauliflower_ear', 'white_discharge'],
    'parvo': ['severe_diarrhea', 'lethargy', 'vomiting', 'dehydration', 'blood_in_stool', 'especially_odorous_feces'],
    'patellar_luxation': ['difficulty_walking', 'difficulty_getting_up', 'weight_off_one_leg'],
    'periodontitis': ['loose_teeth', 'bad_breath', 'tooth_pain', 'sneezing', 'nasal_discharge', 'tooth_loss'],
    'periapical_abscess': ['halitosis', 'discolored_teeth', 'swollen_gums', 'facial_swelling'],
    'proliferating_gum_disease': ['increased_gum_height_thickness', 'gum_bleeding', 'bad_breath', 'excessive_drooling', 'decreased_appetite'],
    'pruritus': ['insatiable_scratching_rubbing_chewing_licking'],
    'pyoderma': ['red_inflamed_patches', 'hot_spots', 'redness_papules_pustules', 'scabbed_lesions',
                 'pain_in_infected_area', 'infection_warm_to_touch', 'red_streaks_on_skin', 'pus_pockets'],
    'rabies': ['lethargy', 'fever', 'vomiting', 'excessive_drooling', 'sensitivity', 'odd_behavior', 'hallucinations', 'self_mutilation', 'ataxia'],
    'ringworm': ['dry_scaly_missing_patches', 'lesions'],
    'roundworm': ['diarrhea', 'pot_bellied_appearance', 'vomiting', 'cough', 'weight_loss', 'dull_coat', 'blocked_intestine'],
    'sarcoptic_mange': ['persistent_itching', 'redness', 'scabs', 'sores'],
    'sebaceous_adenitis': ['stinking_sores', 'scaling_skin', 'hair_loss', 'lesions_head_neck_back', 'itchiness', 'purplish_skin'],
    'spondylosis': ['stiffness', 'limping', 'restricted_movement', 'sensitivity_to_touch', 'back_pain', 'spine_growths'],
    'tapeworm': ['diarrhea', 'loss_of_appetite', 'vomiting', 'weight_loss', 'irritability', 'tapeworm_in_stool'],
    'upper_respiratory_infection': ['sneezing', 'eye_nose_throat_discharge', 'fever', 'drooling', 'difficulty_swallowing', 'dry_cough'],
    'vestibular_disorder': ['walking_in_circles', 'stumbling', 'lack_of_coordination', 'head_tilting', 'wide_exaggerated_stance',
                            'falling_or_rolling', 'nystagmus', 'abnormal_eye_alignment', 'vomiting', 'motion_sickness',
                            'loss_of_appetite', 'sleeping_on_hard_surfaces', 'sleeplessness'],
    'von_willebrand_disease': ['bleeding_gums', 'bloody_urine', 'frequent_nosebleeds', 'easy_bruising', 'clotting_inability'],
    'whipworm': ['bloody_diarrhea', 'dehydration', 'weight_loss', 'lethargy', 'anemia'],
}

# 1. Get a sorted list of all unique symptoms
all_symptoms = sorted({symptom for symptoms in disease_symptoms.values() for symptom in symptoms})

# 2. Create the dataframe
data = []
for disease, symptoms in disease_symptoms.items():
    row = {symptom: (1 if symptom in symptoms else 0) for symptom in all_symptoms}
    row['disease'] = disease
    data.append(row)

df = pd.DataFrame(data)

# 3. Move 'disease' column to the first
df = df[['disease'] + [col for col in df.columns if col != 'disease']]

# 4. Save to CSV
df.to_csv('dataset/disease_symptoms.csv', index=False)

print("✅ CSV file 'disease_symptoms.csv' has been created successfully!")

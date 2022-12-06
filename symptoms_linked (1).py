import random
data = {
    "years_of_education": {"ques": "What is your level of education?",
             "ans": {"low": random.randrange(0,10), "medium": random.randrange(10,15), "high": random.randrange(15,20)},
             "disease": "alzheimer"
            },
    
    "socioeconomic_status": {"ques": "How would you describe your socio-economic status?",
                             "ans": {"low": random.randrange(1.0,3.0), "decent": 3.0, "good": random.randrange(4.0,6.0)},
                             "disease": "alzheimer"
            },
    
    "clinical_dementia_rating": {"ques": "How severe would you describe your loss of memory?",
             "ans": {"not much": random.randrange(0.0,2.0), "bad": random.randrange(2.0,3.0), "quite bad": random.randrange(3.0,6.0)},
             "disease": "alzheimer"
            },
    
    "intracranial_volume": {"ques": "How difficult is it for you to perform everyday tasks?",
             "ans": {"not much": random.randrange(1600,2000), "sometimes_difficult": random.randrange(1300,1600), "very difficult": random.randrange(1100,1300)},
             "disease": "alzheimer"
            },
    
    "norm_brain_volume": {"ques": "How difficult is it for you to perform everyday tasks?",
                          "ans": {"not much": random.uniform(0.750,0.850), 
                                  "sometimes_difficult":random.uniform(0.700,0.750),"very difficult":random.uniform(0.600,0.700)},
                          "disease": "alzheimer"
            },
    
    "atlas_scaling": {"ques": "How difficult is it for you to perform everyday tasks?",
                      "ans": {"not much": random.uniform(1.300,1.600), "sometimes_difficult": random.uniform(1.100,1.300), 
                              "very difficult": random.uniform(0.800,1.100)},
                      "disease": "alzheimer"
            }, 
    
    "mental_state_examination": {"ques": "How difficult is it for you to perform everyday tasks?",
             "ans": {"not much": random.uniform(4.0,12.00), "sometimes_difficult": random.uniform(12.0,21.0), "very difficult": random.uniform(21.0,30.0)},
             "disease": "alzheimer"
            },
    "smoking": {"ques": "Do you smoke?", "ans": {"yes": 2, "no": 1}, "disease": "lung_cancer"},
    "yellow_fingers": {"ques": "Do you have yellow fingers?", "ans": {"yes": 2, "no": 1}, "disease": "lung_cancer"},
    "anxiety": {"ques": "Do you suffer from anxiety?", "ans": {"yes": 2, "no": 1}, "disease": "lung_cancer"},
    "peer_pressure": {"ques": "Do you feel pressured from your peers?", "ans": {"yes": 2, "no": 1}, "disease": "lung_cancer"},
    "chronic_disease": {"ques": "Do you have any chronic disease?", "ans": {"yes": 2, "no": 1}, "disease": "lung_cancer"},
    "fatigue_": {"ques": "Do you get tired easily?", "ans": {"yes": 2, "no": 1}, "disease": "lung_cancer"},
    "allergy_": {"ques": "Do you have allergies?", "ans": {"yes": 2, "no": 1}, "disease": "lung_cancer"},
    "wheezing": {"ques": "Do you wheeze while breathing?", "ans": {"yes": 2, "no": 1}, "disease": "lung_cancer"},
    "alcohol_consuming": {"ques": "Do you consume alcohol?", "ans": {"yes": 2, "no": 1}, "disease": "lung_cancer"},
    "coughing": {"ques": "Do you cough?If yes, Is it bad?", "ans": {"yes": 2, "no": 1}, "disease": "lung_cancer"},
    "shortness_of_breath": {"ques":"Do you experience shortness of breath","ans": {"yes": 2, "no": 1}, "disease": "lung_cancer"},
    "swallowing_difficulty": {"ques": "Do you have problems in swallowing?","ans":{"yes": 2, "no": 1},"disease": "lung_cancer"},
    "chest_pain": {"ques": "Do you have chest pain?", "ans": {"yes": 2, "no": 1}, "disease": "lung_cancer"},
    "ChestPainType": {"ques": "Does your pain lessen when you take stress reliever medicine?", "ans": {"yes, my pain subsides with medicine": "TA", "no, medicine doesn't help": "ATA", "I dont have chest pain related symptoms": "ASY", "pain subsides itself after a while": "NAP"}, "disease": "HeartDisease"},
    "RestingBP": {"ques": "Could you specify your Resting Blood Pressure here?", "ans": {"high": random.randrange(140,200), "normal": random.randrange(80,120) }, "disease": "HeartDisease"},
    "Cholesterol": {"ques": "Could you specify your Cholesterol here?", "ans": {"high": 150, "normal": 70}, "disease": "HeartDisease"},
    "FastingBS": {"ques": "Is your Fasting Blood Sugar>120?", "ans": {"yes": 1, "no": 0}, "disease": "HeartDisease"},
    "RestingECG": {"ques": "Could you specify your Cholesterol here?", "ans": {"normal": "Normal", "LVH": "LVH", "ST": "ST"}, "disease": "HeartDisease"},
    "MaxHR": {"ques": "Could you specify your Cholesterol here?", "ans": {"high": 120, "normal": 70}, "disease": "HeartDisease"},
    "ExerciseAngina":{"ques":"Does your problem aggravate while exercising?",
                      "ans":{"yes":"Y","no":"N"},"disease": "HeartDisease"},
    "Oldpeak": {"ques": "Is your Oldpeak bad?", "ans": {"yes": 4, "no": 1}, "disease": "HeartDisease"},
    "ST_Slope": {"ques": "How severe would you describe your problem while exercising?", "ans": {"not much": "Down", "bad": "Flat", "very bad": "Up"}, "disease": "HeartDisease"},
    "Hypertension": {"ques": "Do you suffer from hypertension?", "ans": {"yes": 1, "no": 0}, "disease": "Stroke"},
    "Heart_disease": {"ques": "Do you any heart related disease?", "ans": {"yes": 1, "no": 0}, "disease": "Stroke"},
    "Smoking_status": {"ques": "Do you smoke?", "ans": {"I did in the past": "formerly smoked", "never": "never smoked", "yes": "smokes", "don't want to disclose": "Unknown"}, "disease": "Stroke"},
    "Ever_married": {"ques": "Are you married?", "ans": {"yes": "yes", "no": "no"}, "disease": "Stroke"},
    "Work_type": {"ques": "Where do you work?", "ans": {"Private": "Private", "Self-employed": "Self-employed", "Dependent": "children", "Govt_job": "Govt_job"}, "disease": "Stroke"},
    "Residence_type": {"ques": "Are you located in urban/ rural area?", "ans": {"Urban": "Urban", "no": 1}, "disease": "Stroke"},
    "Avg_glucose_level": {"ques": "Do you have sugar?", "ans": {"yes": 200, "no": 120}, "disease": "Stroke"},
    "Bmi": {"ques": "Is your BMI good?", "ans": {"yes": 30, "no": 18}, "disease": "Stroke"}
    
}
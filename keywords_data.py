alzheimer_keywords = ["Memory loss", "Poor judgment", "Loss of spontaneity",
                          "Taking longer to complete normal daily tasks", "getting lost", 
                          "Increased anxiety", "Chest pain", "forget things", "can't remember"]
                          
heart_keywords = ["Chest pain","chest tightness", "Shortness of breath", "chest discomfort", "chest pressure", 
                  "Numbness in the legs or arms", "Pain in upper belly area", "Lightheadedness","Dizziness", 
                  "fast heartbeat", "palpitations", "Pain in the neck or back", "Swollen legs"]

lung_cancer_keywords = ["Chronic coughing", "Chest pain", "Shortness of breath","Coughing up blood", 
                            "Wheezing", "Coughing up blood", "Tiredness", "Weight loss", "Bone pain", "Headache"]

stroke_keywords = ["Numbness or weakness in the face, arm, or leg", "Confusion", "Trouble with speaking", 
            "Difficulty in understanding speech", "Trouble seeing in one or both eyes", 
            "Trouble with walking", "Dizziness", "Loss of balance or lack of coordination",
            "Severe headache"]

keywords_dict = {"alzheimer": alzheimer_keywords, "HeartDisease": heart_keywords, "lung_cancer": lung_cancer_keywords, "Stroke": stroke_keywords}

all_keywords = alzheimer_keywords+heart_keywords+lung_cancer_keywords+stroke_keywords





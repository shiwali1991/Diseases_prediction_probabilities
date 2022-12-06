import streamlit as st
import pandas as pd
from symptoms_linked import data
from keywords_data import keywords_dict, all_keywords
import joblib
from fuzzywuzzy import fuzz
from streamlit_tags import st_tags, st_tags_sidebar

st.title("OMEN", "text-align: center")
st.subheader("We are happy to help you today.\
 Please choose the number of health problems that you are experiencing by sliding below\
     \.You will be able to enter your problem in short keywords. Leave rest to us.", "font-size: 30px")


tab1, tab2, tab3 = st.tabs(["General Information", "Questions", "Predictions"])

with tab1:

    

    
    
    
    
    maxtags = st.slider('Please slide here for the number of problems:', 1, 10, 3, key='jfnkerrnfvikwqejn')
    
    st.subheader("Please feel free to specify your problems in the box below:")
    keywords_ = st_tags(
    label='# Enter Keywords:',
    text='Press enter to add more',
    value=['Tiredness', "chest pain"],
    suggestions= all_keywords,
    maxtags=maxtags,
    key="aljnf")
    
    disease_dict = {}
    
                 
    for item in keywords_:
        for key, value in keywords_dict.items():
            if item in value:
                disease_dict[key] = {"dataset": pd.read_csv(f"final_{key}.csv"), 
                                     "model": joblib.load(f'model_pipeline_{key}.pkl')}
            else:
                for item_ in value:
                    match_ratio = fuzz.token_sort_ratio(item,item_)
                    if match_ratio>=70:
                        
                        disease_dict[key] = {"dataset": pd.read_csv(f"final_{key}.csv"), 
                                     "model": joblib.load(f'model_pipeline_{key}.pkl')}
                        #st.write(item, match_ratio, item_) 
                        

    age = st.number_input("Please mention your age", min_value=0, max_value=100)
    gender = st.selectbox("Are you male/female", options = ["M", "F"])

    def store_symptoms(data_dict):
        results = {}
        for key, value in data_dict.items():
            if value["disease"] in list(disease_dict.keys()):
                question = value["ques"]
                possible_answers = value["ans"]
                result = st.selectbox(question, list(possible_answers.keys()), key = key)
                result1 = possible_answers[result]
                results[key] = result1
        return results

    patient_input = {"age": age, "sex": gender}
    st.subheader("This button would direct you to the next page")
    
    #st.session_state.disabled = True
    

    #if st.button("Please Click Here"):
        
    with tab2:
        x = store_symptoms(data)
        patient_input = {**patient_input, **x}
        #patient_input.update(x)
        patient_data = pd.DataFrame([patient_input])
        #st.write(patient_data)
     
        
           
    with tab3:

        def predict_diseases(patient_data):
            probabilities = {}
            for key, value in disease_dict.items():            
                model = value["model"]
                df = value["dataset"].drop(columns = key, axis = 1)            
                cols = list(df.columns)                    
                patient_data_ = patient_data[cols]     
                y_test_pred = model.predict(patient_data_)                        
                prob = model.predict_proba(patient_data_)
                probabilities[key] = prob[0][1]
            return probabilities

        prob_ = predict_diseases(patient_data)
        prob_df = pd.DataFrame.from_dict(prob_, orient='index', columns=["Probability(%)"])
        prob_df["Probability(%)"] = round(prob_df["Probability(%)"]*100, 2) # Getting the percentages
        st.bar_chart(prob_df)

        st.write(prob_) 







#st.subheader("Please click on the following button to answer a few questions to help us understand your problem better")

    

    
        
        

        

   

    
        
        
       
    



        

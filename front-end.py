import streamlit as st
import joblib
import pandas as pd

# Load the saved model
model = joblib.load('placement_predictor_model.pkl')

st.title("🎓 Indian Campus Placement Predictor")
st.write("Enter your details to predict your placement probability.")

# Create input fields for your parameters
cgpa = st.slider("College CGPA", 0.0, 10.0, 8.0)
coding_skill = st.slider("Coding Skill Rating (1-10)", 1, 5, 3)
Attendance = st.number_input("Attendance", 0, 100, 0)
projects = st.number_input("Number of Projects Done", 0, 20, 0)
internships = st.number_input("Number of Internships Done", 0, 10, 0)
hackathons_participated = st.number_input("Number of times Participated in Hackathons", 0, 10, 0)
certifications_count = st.number_input("Number of Certificets", 0, 20, 0)

# When the button is clicked
if st.button("Predict My Future"):
    # Create a dataframe for the input (must match X_train columns exactly)
    query = pd.DataFrame([[cgpa, coding_skill]], 
                         columns=['cgpa', 'coding_skill_rating'])
    
    prediction = model.predict(query)
    
    if prediction[0] == 1:
        st.success("Congratulations! You are likely to be PLACED.")
    else:
        st.error("Warning: High risk of not being placed. Focus on skills!")
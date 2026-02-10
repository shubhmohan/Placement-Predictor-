import streamlit as st
import pandas as pd
import joblib
import numpy as np

# -----------------------------------------------------------------------------
# 1. PAGE CONFIGURATION (Must be the first command)
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="FutureSight | Placement Predictor",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------------------------------------------------------
# 2. CUSTOM CSS (The "Black Mesh" & Bluish Theme)
# -----------------------------------------------------------------------------
st.markdown("""
<style>
    /* Main Background - Dark with a subtle gradient mesh feel */
    .stApp {
        background-color: #0E1117;
        background-image: radial-gradient(circle at 50% 50%, #1d2636 0%, #0E1117 100%);
    }

    /* Typography - Bluish Tone */
    h1, h2, h3 {
        color: #4DB7FE !important;
        font-family: 'Segoe UI', sans-serif;
        text-shadow: 0px 0px 10px rgba(77, 183, 254, 0.3);
    }
    
    p, label {
        color: #C5D1E0 !important;
    }

    /* Input Fields Styling */
    .stSlider > div > div > div > div {
        background-color: #0078D7;
    }
    
    .stSelectbox > div > div {
        background-color: #161B22;
        color: white;
        border: 1px solid #4DB7FE;
    }
    
    .stNumberInput > div > div > input {
        background-color: #161B22;
        color: white;
        border: 1px solid #4DB7FE;
    }

    /* Custom Button Style */
    div.stButton > button {
        background: linear-gradient(90deg, #0062CC 0%, #00A3E0 100%);
        color: white;
        border: none;
        padding: 12px 24px;
        font-size: 18px;
        font-weight: bold;
        border-radius: 8px;
        box-shadow: 0px 4px 15px rgba(0, 163, 224, 0.4);
        transition: all 0.3s ease;
        width: 100%;
    }
    
    div.stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0px 6px 20px rgba(0, 163, 224, 0.6);
        background: linear-gradient(90deg, #00A3E0 0%, #0062CC 100%);
    }

    /* Result Card Styling */
    .result-card {
        background-color: #161B22;
        padding: 25px;
        border-radius: 15px;
        border-left: 5px solid #4DB7FE;
        box-shadow: 0 4px 6px rgba(0,0,0,0.3);
        margin-top: 20px;
    }
    
    /* Metrics */
    div[data-testid="stMetricValue"] {
        color: #00F0FF !important;
    }
</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 3. SIDEBAR & HEADER
# -----------------------------------------------------------------------------
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/4762/4762311.png", width=80)
    st.title("Student Profile")
    st.markdown("---")
    st.write("Configure the student's academic and technical profile here.")
    st.info("💡 **Tip:** Coding skills and Projects usually carry high weightage!")
    st.markdown("---")
    st.caption("Developed by [Shubh Mohan](https://github.com/shubhmohan)")

st.title("🎓 FutureSight AI")
st.markdown("### ⚡ Intelligent Placement Probability Predictor")
st.write("Enter your academic details below to see your placement chances analyzed by our Random Forest model.")

# -----------------------------------------------------------------------------
# 4. INPUT SECTION (Layout using Columns)
# -----------------------------------------------------------------------------
st.markdown("<br>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("📚 Academics")
    cgpa = st.slider("CGPA (0-10)", 0.0, 10.0, 7.5, 0.1)
    attendance = st.slider("Attendance %", 0, 100, 75)
    
with col2:
    st.subheader("💻 Technical")
    coding_skill = st.slider("Coding Skill (1-5)", 1, 5, 3)
    projects = st.number_input("Projects Completed", 0, 50, 2)
    internships = st.number_input("Internships Completed", 0, 10, 1)

with col3:
    st.subheader("🏆 Extra-Curricular")
    hackathons = st.number_input("Hackathons", 0, 20, 1)
    certifications = st.number_input("Certifications", 0, 20, 1)

st.markdown("<br>", unsafe_allow_html=True)
col_a, col_b = st.columns(2)

with col_a:
    branch = st.selectbox("Engineering Branch", ["CSE", "ECE", "IT", "ME", "Civil", "Other"])

with col_b:
    gender = st.radio("Gender", ["Male", "Female"], horizontal=True)

# -----------------------------------------------------------------------------
# 5. PREDICTION LOGIC
# -----------------------------------------------------------------------------
# List of columns exactly as they appeared in training (from your df.columns)
# ['cgpa', 'attendance_percentage', 'projects_completed', 'internships_completed', 
#  'coding_skill_rating', 'hackathons_participated', 'certifications_count', 
#  'gender_Male', 'branch_CSE', 'branch_ECE', 'branch_IT', 'branch_ME']

def predict_placement():
    # 1. Initialize input dictionary with default 0s
    input_data = {
        'cgpa': cgpa,
        'attendance_percentage': attendance,
        'projects_completed': projects,
        'internships_completed': internships,
        'coding_skill_rating': coding_skill,
        'hackathons_participated': hackathons,
        'certifications_count': certifications,
        'gender_Male': 0,
        'branch_CSE': 0,
        'branch_ECE': 0,
        'branch_IT': 0,
        'branch_ME': 0
    }

    # 2. Handle Categorical Logic (One-Hot Encoding)
    if gender == 'Male':
        input_data['gender_Male'] = 1
    
    if branch == 'CSE':
        input_data['branch_CSE'] = 1
    elif branch == 'ECE':
        input_data['branch_ECE'] = 1
    elif branch == 'IT':
        input_data['branch_IT'] = 1
    elif branch == 'ME':
        input_data['branch_ME'] = 1
    # Note: 'Other' or 'Civil' will leave all branch columns as 0

    # 3. Convert to DataFrame
    df_input = pd.DataFrame([input_data])

    try:
        # 4. Load Model
        model = joblib.load('placement_predictor_model.pkl')
        
        # 5. Predict
        prediction = model.predict(df_input)[0]
        probability = model.predict_proba(df_input)[0][1] # Probability of Class 1 (Placed)

        return prediction, probability

    except FileNotFoundError:
        st.error("⚠️ Model file not found! Please make sure 'placement_predictor_model.pkl' is in the same directory.")
        return None, None

# -----------------------------------------------------------------------------
# 6. ACTION BUTTON & UI
# -----------------------------------------------------------------------------
st.markdown("---")
if st.button("🚀 Analyze Profile"):
    with st.spinner("Crunching the numbers..."):
        status, prob = predict_placement()

    if status is not None:
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Result Display
        if status == 1:
            st.balloons()
            st.markdown(f"""
            <div class="result-card" style="border-left: 5px solid #00FF7F;">
                <h2 style="color: #00FF7F !important; margin:0;">🎉 Likely to be PLACED!</h2>
                <p style="font-size: 18px;">Great job! Your profile looks strong for the current market.</p>
                <h1 style="color: white !important;">{prob:.1%} Chance</h1>
            </div>
            """, unsafe_allow_html=True)
            
            # Progress Bar
            st.progress(int(prob * 100))
            
        else:
            st.markdown(f"""
            <div class="result-card" style="border-left: 5px solid #FF4B4B;">
                <h2 style="color: #FF4B4B !important; margin:0;">⚠️ Needs Improvement</h2>
                <p style="font-size: 18px;">Don't worry! Focus on building more projects and improving coding skills.</p>
                <h1 style="color: white !important;">{prob:.1%} Chance</h1>
            </div>
            """, unsafe_allow_html=True)
            
            st.progress(int(prob * 100))
            
            # Improvement Tips
            with st.expander("📈 How to improve your chances?"):
                st.write("- **Increase Coding Rating:** Practice DSA on LeetCode/CodeChef.")
                st.write("- **Build Projects:** Aim for at least 3-4 full-stack or ML projects.")
                st.write("- **Internships:** Try to get at least one industrial experience.")
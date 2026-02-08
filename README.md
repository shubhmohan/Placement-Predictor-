# 🎓 College Placement Predictor

<div align="center">
  <a href="https://github.com/shubhmohan">
    <img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&height=250&section=header&text=Placement%20Predictor&fontSize=80&animation=fadeIn&fontAlignY=35&desc=AI-Powered%20Career%20Forecasting%20Tool&descAlignY=55&descAlign=50" alt="Shubh Mohan's GitHub Banner" width="100%"/>
  </a>
</div>

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)](https://streamlit.io/)
[![Scikit-Learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](./LICENSE)

**_Will you get placed? Let AI analyze your academic & technical profile to find out._**

[View Demo](#-demo) • [Installation](#-installation--usage) • [Key Features](#-key-features) • [Change Log](#-change-log)

</div>

---

## 🧐 About The Project

The **College Placement Predictor** is a machine learning tool designed to help engineering students understand their employability. 

Unlike generic calculators, this project uses a **Random Forest Classifier** trained on real student data (including academic history, coding skills, and internships) to predict the likelihood of placement. It bridges the gap between **Academic Performance** and **Industry Requirements**.

---

## 🚀 Key Features

* **🎯 High-Accuracy Predictions:** Uses an optimized Random Forest model to analyze complex student patterns.
* **📊 Interactive Dashboard:** Built with **Streamlit** for a seamless, no-code UI experience.
* **🧠 "Skill vs. Grades" Analysis:** Weighs the impact of **Coding Skills** and **Projects** against traditional **CGPA** and **Backlogs**.
* **⚡ Real-Time Probability:** Doesn't just say "Yes/No" — provides a **Confidence Score** (e.g., *"85% chance of placement"*).
* **📈 Visual Insights:** Includes charts to visualize which factors are hurting or helping your chances.

---

## 🛠️ Tech Stack

| Component | Technology |
| :--- | :--- |
| **Language** | Python 3.x |
| **Frontend** | Streamlit |
| **ML Model** | Scikit-Learn (Random Forest) |
| **Data Processing** | Pandas, NumPy |
| **Visualization** | Matplotlib, Seaborn |
| **Deployment** | Streamlit Cloud (Ready) |

---

## 💻 Installation & Usage

Follow these simple steps to run the project on your local machine.

### Prerequisites
* Python installed on your system.
* Git installed.

### Step 1: Clone the Repository
```bash
git clone [https://github.com/shubhmohan/Placement-Predictor.git](https://github.com/shubhmohan/Placement-Predictor.git)
cd Placement-Predictor
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```
<<<<<<< HEAD

=======
>>>>>>> d24c9b4d84b18230bc28552e0295a70a5115069b
### Step 3: Launcch the APP
```bash
streamlit run app.py 
```

## 📸 Demo
----

### 📅 Change Log
[v1.2.0] - 2026-02-08
🚀 Feature: Added "One-Hot Encoding" for better handling of branch and gender data.

🎨 UI: Redesigned the Streamlit sidebar for better navigation.

🐛 Fix: Resolved NaN handling for salary columns in the dataset.

[v1.1.0] - 2026-02-02
✨ Feature: Integrated coding_skill_rating into the prediction logic.

📊 Viz: Added "Feature Importance" chart to show what matters most.

[v1.0.0] - 2026-01-30
🎉 Initial Release: Basic prediction using CGPA and Backlogs.

## 📬 Contact
Shubh Mohan - GitHub: github.com/shubhmohan

LinkedIn: [Your LinkedIn Profile Here]

<div align="center"> <sub>Built with ❤️ by Shubh Mohan</sub> </div>

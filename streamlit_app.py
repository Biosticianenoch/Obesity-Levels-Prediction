import pickle
import os
import numpy as np
import streamlit as st
from streamlit_option_menu import option_menu
import datetime

# ---------------- CONFIG ----------------
st.set_page_config(page_title="Obesity Level Classifier", layout="centered")

# ---------------- LOAD MODEL ----------------
model = pickle.load(open("obesity.sav", 'rb'))

# ---------------- VISITOR COUNTER ----------------
counter_file = "visitor_data.pkl"

if os.path.exists(counter_file):
    with open(counter_file, 'rb') as f:
        visitor_data = pickle.load(f)
else:
    visitor_data = {'count': 0, 'timestamps': []}

if 'counted' not in st.session_state:
    st.session_state['counted'] = True
    visitor_data['count'] += 1
    visitor_data['timestamps'].append(str(datetime.datetime.now()))
    with open(counter_file, 'wb') as f:
        pickle.dump(visitor_data, f)

# ---------------- SIDEBAR MENU ----------------
with st.sidebar:
    selected = option_menu("Main Menu", 
                           ["Welcome", "Prediction", "Recommendation", "FAQ", "Disclaimer", "Analytics"], 
                           icons=['house', 'activity', 'heart', 'question-circle', 'exclamation-circle', 'bar-chart'],
                           menu_icon="cast", default_index=0)

# ---------------- WELCOME PAGE ----------------
if selected == "Welcome":
    st.markdown("<h1 style='text-align: center; color: crimson;'>🏥 Obesity Risk Classifier</h1>", unsafe_allow_html=True)
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOXMzYTBsNzB0OXE0aG84b2tkZzA2aGFscjhiOXlyemFhbmp1OXZ4ZSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/qh4sUO8gO0Pfy/giphy.gif", use_column_width=True)
    st.success(f"🎉 **Total Visitors:** {visitor_data['count']}")
    st.write("""
    This intelligent tool helps classify a person's obesity level using health and lifestyle inputs.

    ✅ Quick prediction  
    ✅ Personalized recommendations  
    ✅ Supports healthy lifestyle changes

    👉 Use the sidebar to begin your screening process!
    """)

# ---------------- PREDICTION PAGE ----------------
elif selected == "Prediction":
    st.markdown("<h2 style='text-align: center;'>🧮 Obesity Level Prediction</h2>", unsafe_allow_html=True)
    st.write("Fill in the following health and lifestyle information:")

    with st.form("obesity_form"):
        gender = st.selectbox("Gender", [0, 1], format_func=lambda x: "Female" if x == 0 else "Male")
        age = st.number_input("Age", min_value=1)
        height = st.number_input("Height (meters)", min_value=0.5, format="%.2f")
        weight = st.number_input("Weight (kg)", min_value=10.0)
        family_history = st.selectbox("Family History of Overweight", [0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
        favc = st.selectbox("High Caloric Food Consumption (FAVC)", [0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
        fcvc = st.slider("Frequency of Vegetable Consumption (FCVC)", 1.0, 3.0, step=0.1)
        ncp = st.slider("Number of Main Meals (NCP)", 1.0, 4.0, step=0.5)
        caec = st.selectbox("Eating Between Meals (CAEC)", [0, 1, 2, 3], format_func=lambda x: ["No", "Sometimes", "Frequently", "Always"][x])
        smoking = st.selectbox("Do You Smoke?", [0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
        water = st.number_input("Daily Water Intake (litres) (CH2O)", min_value=0.0, step=0.1)
        scc = st.selectbox("Do You Monitor Calories (SCC)?", [0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
        physical_activity = st.selectbox("Physical Activity Frequency (FAF)", [0, 1, 2], format_func=lambda x: ["None", "Moderate", "High"][x])
        tech_hours = st.number_input("Hours Using Technology per Day (TUE)", min_value=0.0, step=0.5)
        calc = st.selectbox("Alcohol Consumption (CALC)", [0, 1, 2], format_func=lambda x: ["No", "Sometimes", "Frequently"][x])
        transport = st.selectbox("Transportation Mode (MTRANS)", [0, 1], format_func=lambda x: "Public/Walking" if x == 0 else "Private Vehicle")

        submit = st.form_submit_button("Predict Obesity Level")

    if submit:
        input_data = np.array([[gender, age, height, weight, family_history, favc,
                                fcvc, ncp, caec, smoking, water, scc,
                                physical_activity, tech_hours, calc, transport]])

        prediction = model.predict(input_data)[0]

        class_mapping = {
            0: "Underweight",
            1: "Normal Weight",
            2: "Overweight Level I",
            3: "Overweight Level II",
            4: "Obesity Type I",
            5: "Obesity Type II",
            6: "Obesity Type III"
        }

        result = class_mapping.get(prediction, "Unknown")
        st.success(f"🏷️ **Predicted Obesity Level:** {result}")

# ---------------- RECOMMENDATION PAGE ----------------
elif selected == "Recommendation":
    st.markdown("<h2 style='text-align: center;'>💡 Health Recommendations</h2>", unsafe_allow_html=True)
    st.write("""
    Based on the prediction, here are some recommendations:

    - 🥗 **Adopt a healthy diet**: More vegetables, fruits, and fiber.
    - 🏃 **Be active**: At least 30 minutes daily.
    - 💧 **Hydrate well**: Drink 2+ liters per day.
    - 🚭 **Avoid smoking and excess alcohol**.
    - 📋 **Track your calories** using apps or journals.
    - 🧘 **Manage stress** with relaxation techniques.
    
    Always consult a healthcare provider for a personalized plan.
    """)

# ---------------- FAQ PAGE ----------------
elif selected == "FAQ":
    st.markdown("<h2 style='text-align: center;'>❓ Frequently Asked Questions</h2>", unsafe_allow_html=True)

    with st.expander("📌 What does this app do?"):
        st.write("This app classifies your obesity level based on several health and lifestyle inputs.")

    with st.expander("📌 Is it a medical diagnostic tool?"):
        st.write("No. This is a predictive tool and does not replace professional diagnosis.")

    with st.expander("📌 Is my data stored?"):
        st.write("No data is stored or sent to a server. Everything runs locally in your browser.")

    with st.expander("📌 Can I use this app on my phone?"):
        st.write("Yes, this app is mobile-responsive and works on smartphones and tablets.")

    with st.expander("📌 What model is used for prediction?"):
        st.write("A machine learning model trained on anonymized health and lifestyle data.")

    with st.expander("📌 What if I get an unexpected result?"):
        st.write("Results are based on patterns in the data. Always consult a healthcare provider for confirmation.")

# ---------------- DISCLAIMER PAGE ----------------
elif selected == "Disclaimer":
    st.markdown("<h2 style='text-align: center;'>⚠️ Disclaimer</h2>", unsafe_allow_html=True)
    st.warning("""
    - This app is strictly for screening and awareness purposes.
    - It does not offer a certified medical opinion.
    - Always seek professional medical advice.
    - The developers are not responsible for health decisions made based on this tool.
    """)

# ---------------- ANALYTICS PAGE ----------------
elif selected == "Analytics":
    st.markdown("<h2 style='text-align: center;'>📊 Visitor Analytics</h2>", unsafe_allow_html=True)

    st.info(f"👥 **Total Visitors:** {visitor_data['count']}")

    if visitor_data['timestamps']:
        st.write("### 🕒 Visitor Log")
        st.dataframe(visitor_data['timestamps'])

    if st.button("🔄 Reset Visitor Counter"):
        visitor_data = {'count': 0, 'timestamps': []}
        with open(counter_file, 'wb') as f:
            pickle.dump(visitor_data, f)
        st.success("Visitor counter reset. Please refresh to see update.")

    st.caption("Note: Data is stored locally in `visitor_data.pkl`. No external tracking involved.")

# ---------------- DONATION PAGE ----------------
elif selected == "Donate 💖":
    st.markdown("<h2 style='text-align: center;'>💖 Support My Work</h2>", unsafe_allow_html=True)

    st.write("""
    If you found this app helpful and would like to support its development and maintenance, consider donating 🙏

    Your contribution will help in:
    - Maintaining the hosting of this tool
    - Enhancing features & user experience
    - Creating similar free health tech tools

    **Donate via PayPal:**  
    [![Donate](https://img.shields.io/badge/Donate-PayPal-blue.svg)](https://www.paypal.com/donate/?hosted_button_id=YOUR_BUTTON_ID)

    **Buy me a coffee:**  
    [Buy Me a Coffee ☕](https://www.buymeacoffee.com/YOUR_USERNAME)

    **M-Pesa Paybill (Kenya):**  
    - **Paybill:** 123456  
    - **Account Number:** OBESITYAPP

    Every donation, no matter how small, makes a difference ❤️  
    """)

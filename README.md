
# 🏥 Obesity Level Classifier – ML-Powered Health Risk Screening App 💡

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Web_App-red?logo=streamlit)
![Model](https://img.shields.io/badge/ML_Model-RandomForest-orange?logo=scikit-learn)
![License](https://img.shields.io/badge/License-MIT-green.svg)

> A smart health application that predicts **Obesity Risk Levels** using personalized inputs including biometric and lifestyle habits, built with Machine Learning and deployed using Streamlit.

---

## ✨ Features

✅ Predicts obesity class (7 levels) with a trained ML model  
✅ Sleek and responsive Streamlit web interface  
✅ Tracks user visits with persistent visitor counter  
✅ Offers personalized health tips and best practices  
✅ Local-first: No data sent to a server  
✅ Interactive sidebar navigation with `streamlit-option-menu`  

---

## 📸 App Snapshot

![App Screenshot](https://media.giphy.com/media/qh4sUO8gO0Pfy/giphy.gif)

---

## 🚀 How to Run the App

### 🔧 Setup

1. Clone this repo  
2. Install requirements:  
```bash
pip install -r requirements.txt
```

3. Launch the app:  
```bash
streamlit run app.py
```

4. Visit `http://localhost:8501` in your browser

---

## 🧠 About the Machine Learning Model

Trained using health and nutrition data, the model classifies users into:

| Label | Classification         |
|-------|------------------------|
| 0     | Underweight            |
| 1     | Normal Weight          |
| 2     | Overweight Level I     |
| 3     | Overweight Level II    |
| 4     | Obesity Type I         |
| 5     | Obesity Type II        |
| 6     | Obesity Type III       |

📦 `obesity.sav` is the exported model used in the app.

---

## 📁 File Structure

```
📂 Obesity-Level-Classifier/
├── app.py                # Streamlit application code
├── obesity.sav           # Trained ML model (Random Forest)
├── obesity.ipynb         # Notebook: Data analysis + model training
├── visitor_data.pkl      # Local file for visitor logging
└── README.md             # You're reading it!
```

---

## 📚 Libraries Used

- `streamlit` – UI framework
- `numpy`, `pandas` – Data handling
- `scikit-learn` – ML model
- `pickle` – Model and counter persistence

---

## 📌 Functional Highlights

- 🧮 **Prediction Page**: Classifies obesity risk level  
- 📋 **Health Tips Page**: Personalized recommendations  
- ℹ️ **FAQ Section**: Answers common questions  
- ⚠️ **Disclaimer**: For ethical transparency  
- 📊 **Analytics Page**: Tracks visitor sessions  

---

## ⚠️ Disclaimer

This tool is intended **for educational and awareness purposes only**.  
It does **not** substitute professional medical consultation or treatment.

Always consult a licensed healthcare provider before making any health-related decisions.

---

## 🧑‍💻 Author & Contact

Created with ❤️ by [Your Name]  
🔗 GitHub: [@YourUsername](https://github.com/YourUsername)  
📧 Email: youremail@example.com

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).  
Feel free to use, share, and improve with credit.

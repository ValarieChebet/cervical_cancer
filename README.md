# 🧬 Cervical Cancer Risk Prediction App

An AI-powered, multilingual web application built with Streamlit that predicts the risk of cervical cancer based on patient input. It supports PDF report generation and is accessible online.

🔗 **Live App**: [https://cervicalcancertest.streamlit.app/](https://cervicalcancertest.streamlit.app/)

---

### 🧰 Features

- ✅ **Predicts cervical cancer risk** using a pre-trained machine learning model.
- 🌍 **Multi-language support**: English, Hindi, Spanish, French.
- 📝 **Patient details collection** with an intuitive sidebar form.
- 📋 **Tabbed UI**: One for form entry, another for prediction results.
- 📄 **Downloadable PDF report** including patient inputs and results.
- 🧠 **Model integration**: Easily swap in your own trained `.pkl` model.

---

### 📸 Screenshots

| Input Form | Prediction Tab | PDF Download |
|------------|----------------|--------------|
| ![Form Screenshot](input_app.png) | ![Prediction Screenshot](result_app.png) | ![PDF Screenshot](pdf_app.png) |



---

### 🚀 Getting Started Locally

#### 1. **Clone the Repository**

```bash
git clone https://github.com/yourusername/cervical-cancer-predictor.git
cd cervical-cancer-predictor


2. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
If requirements.txt doesn't exist, manually install:

bash
Copy
Edit
pip install streamlit numpy joblib reportlab
3. Add the Trained Model
Place your cervicalcancer.pkl file in the project root directory. This should be a joblib-serialized scikit-learn model trained to accept input features in the correct order.

4. Run the App
bash
Copy
Edit
streamlit run your_script_name.py
📄 Project Structure
bash
Copy
Edit
📁 cervical-cancer-predictor/
├── cervicalcancer.pkl              # Trained ML model (add your own)
├── your_script_name.py            # Streamlit app code
├── README.md
└── requirements.txt               # Dependency file
🌐 Language Support
This app currently supports the following languages:

English 🇺🇸

Hindi 🇮🇳

Spanish 🇪🇸

French 🇫🇷

Translations can be easily extended via the translations dictionary in the code.

🧠 Model Requirements
Your trained model should expect the following features in order:

csharp
Copy
Edit
[Age, PoR, ES, SES, Parity, AgeFirstP, MC, MH, Contraception, 
 Smoking, HRHPV, IL6, IL1beta, TNFalpha, IL1RN]
All features must be numerically encoded, which is already handled by the app.

📄 PDF Report
The generated report includes:

Patient name and location

Date and time of the prediction

Risk result

All selected form details

PDFs are downloadable directly from the results tab.

📌 Acknowledgements
Model serialization: joblib

Web app framework: Streamlit

PDF generation: ReportLab

📬 Contact
For issues, feel free to open an issue 

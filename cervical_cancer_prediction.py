import streamlit as st
import joblib
import numpy as np
from fpdf import FPDF
import io
from datetime import datetime
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch

# Load model
MODEL_PATH = "logistic_regression_cancer_risk_model.pkl"
model = joblib.load(MODEL_PATH)

# Supported languages
languages = {
    "English": "en",
    "Hindi": "hi",
    "Spanish": "es",
    "French": "fr"
}

# Translation dictionary (partial for demonstration)
translations = {
    "Patient Details": {
        "hi": "रोगी का विवरण",
        "es": "Detalles del paciente",
        "fr": "Détails du patient"
    },
    "Name": {"hi": "नाम", "es": "Nombre", "fr": "Nom"},
    "Location": {"hi": "स्थान", "es": "Ubicación", "fr": "Emplacement"},
    "Country": {"hi": "देश", "es": "País", "fr": "Pays"},
    "Submit": {"hi": "जमा करें", "es": "Enviar", "fr": "Soumettre"},
    "Download PDF Report": {
        "hi": "पीडीएफ रिपोर्ट डाउनलोड करें",
        "es": "Descargar informe PDF",
        "fr": "Télécharger le rapport PDF"
    }
}

def t(text, lang):
    return translations.get(text, {}).get(lang, text)

def create_pdf(patient_name, prediction_result, details):
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4

    c.setFont("Helvetica-Bold", 14)
    c.drawCentredString(width / 2, height - 50, "Cervical Cancer Risk Assessment Report")

    c.setFont("Helvetica", 10)
    c.drawString(40, height - 80, f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    c.drawString(40, height - 100, f"Patient Name: {patient_name}")
    c.drawString(40, height - 120, f"Prediction Result: {'At Risk' if prediction_result == 1 else 'No Risk'}")

    c.setFont("Helvetica-Bold", 12)
    c.drawString(40, height - 150, "Entered Details:")

    y = height - 170
    c.setFont("Helvetica", 10)
    for key, value in details.items():
        if y < 50:
            c.showPage()
            y = height - 50
        c.drawString(60, y, f"{key}: {value}")
        y -= 15

    c.save()
    buffer.seek(0)
    return buffer

# App config
st.set_page_config(page_title="Cervical Cancer Predictor", page_icon="🏥", layout="wide")

# Language selection
selected_lang = st.sidebar.selectbox("🌐 Select Language", list(languages.keys()))
lang_code = languages[selected_lang]

# Title
st.markdown(
    f"<h1 style='text-align: center; color: navy;'>🧬 {'Cervical Cancer Diagnosis Application'}</h1>",
    unsafe_allow_html=True
)

# Sidebar
with st.sidebar:
    st.header(f"👩‍⚕️ {t('Patient Details', lang_code)}")
    user_name = st.text_input(f"📝 {t('Name', lang_code)}")
    user_location = st.text_input(f"📍 {t('Location', lang_code)}")
    user_country = st.text_input(f"🌍 {t('Country', lang_code)}")

# Tabs
tab1, tab2 = st.tabs(["🧾 Input Form", "📊 Prediction Result"])

with tab1:
    with st.form("cervical_form"):
        col1, col2 = st.columns(2)

        with col1:
            age = st.slider("Age", 1, 110, 30)
            sexual_partners = st.slider("Number of Sexual Partners", 0, 50, 1)
            first_sexual_activity_age = st.slider("Age at First Sexual Activity", 10, 50, 18)
            hpv_test_result = st.radio("HPV Test Result", ["Positive", "Negative"])
            pap_smear_result = st.radio("Pap Smear Result", ["Positive", "Negative"])

        with col2:
            smoking_status = st.radio("Smoking Status", ["Never", "Former", "Current"])
            stds_history = st.radio("History of STDs", ["Yes", "No"])
            region = st.radio("Region", ["Urban", "Rural"])
            insurance_covered = st.radio("Insurance Covered", ["Yes", "No"])
            screening_type_last = st.radio("Last Screening Type", ["Pap Smear", "HPV Test", "Both", "None"])

        submitted = st.form_submit_button(t("Submit", lang_code))

        if submitted:
            st.success("✅ Prediction submitted! Go to the next tab to view the result.")

with tab2:
    if submitted:
        hpv_test_result_val = 1 if hpv_test_result == "Positive" else 0
        pap_smear_result_val = 1 if pap_smear_result == "Positive" else 0
        smoking_status_val = {"Never": 0, "Former": 1, "Current": 2}[smoking_status]
        stds_history_val = 1 if stds_history == "Yes" else 0
        region_val = 1 if region == "Urban" else 0
        insurance_covered_val = 1 if insurance_covered == "Yes" else 0
        screening_type_last_val = {"Pap Smear": 0, "HPV Test": 1, "Both": 2, "None": 3}[screening_type_last]

        input_data = np.array([[age, sexual_partners, first_sexual_activity_age, hpv_test_result_val, 
                                pap_smear_result_val, smoking_status_val, stds_history_val, 
                                region_val, insurance_covered_val, screening_type_last_val]])

        result = model.predict(input_data)
        patient_display = user_name.strip() if user_name else "Patient"

        st.markdown("### 🧪 Prediction Result")
        if result[0] == 1:
            st.error(f"🔬 {patient_display}, you may have a risk of Cervical Cancer.")
        else:
            st.success(f"✅ {patient_display}, no indication of Cervical Cancer risk was found.")
            st.balloons()

        # Generate and download PDF
        patient_details = {
            "Name": user_name,
            "Location": user_location,
            "Country": user_country,
            "Age": age,}
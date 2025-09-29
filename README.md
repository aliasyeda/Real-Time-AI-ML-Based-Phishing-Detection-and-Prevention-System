# 🛡️ Real-Time AI/ML-Based Phishing Detection and Prevention System

**Smart India Hackathon 2025**  
**Problem Statement: Real-Time AI/ML-Based Phishing Detection and Prevention System (PS #25159)**  

---

## 📌 OVERVIEW  
Phishing attacks are one of the most common cyber threats.  
 **Real-time AI/ML phishing detection and prevention system** built as a **Streamlit web application**.  

Our logistic regression model (with TF-IDF) achieves **~99% accuracy** and classifies input as:  
- ✅ Safe  
- ⚠ Suspicious  
- 🚨 Phishing  

Unlike Gmail or VirusTotal, this system is **explainable and educational**: it shows keywords, risky domains, confidence scores, and provides awareness training through a quiz.  

---

## 🚀 FEATURES  

- **AI / ML Model (scikit-learn)**  
  - Logistic Regression trained on phishing **emails + URLs** datasets  
  - Hybrid rules with trusted domains to reduce false positives  

- **Web App (Streamlit)**  
  - 🛡️ Detector: Paste text/URL or upload `.txt` file  
  - 📊 Dashboard: Stats with bar chart + donut chart  
  - 💡 Awareness Quiz: Tips + 5-question awareness quiz  

- **Explainable & User-Friendly**  
  - Confidence score (%)  
  - Highlight suspicious keywords  
  - Analysis of domain names  
  - Light/Dark mode toggle, color-coded result cards  

---

## 🛠️ TECH STACK  

- **Language:** Python 3.10+  
- **Libraries:**  
  - `streamlit`, `scikit-learn`, `pandas`, `numpy`, `plotly`  

---

## 📂 PROJECT STRUCTURE  
Real-Time-AI-ML-Based-Phishing-Detection-and-Prevention-System
│
├── app.py # Streamlit web app
├── phishing_combined_model.pkl # Trained ML model (Logistic Regression)
├── vectorizer_vocab.json # Lightweight TF-IDF vocabulary for deployment
├── phishing_model_training.ipynb # Jupyter Notebook (model training & saving files)
├── requirements.txt # List of dependencies for Streamlit Cloud deployment
├── sample_safe_email.txt # Demo input file: Safe email
├── sample_phish_email.txt # Demo input file: Phishing email
└── sample_suspicious_email.txt # Demo input file: Suspicious emai

## 🎯 DEMO SAMPLES  

**✅ Safe Email Example**

Your Amazon order has been shipped:

https://www.amazon.in/order




**🚨 Phishing Email Example**

Urgent! Your PayPal account is limited, verify here:

http://secure-login-paypai.com




**⚠ Suspicious Email Example**

We detected unusual activity in your account.

Please review your profile details.




---

## 🚀 FUTURE SCOPE  

- Gmail/Outlook integration → automatically move phishing mails to spam  
- Browser extension for **real-time URL scanning**  
- Multi-language phishing awareness training modules  
- Enterprise dashboards for monitoring phishing attempts  

---

## 👥 TEAM  

Smart India Hackathon 2025 – *Team Name*  


- Member 1: ISMAIL ALI MOHAMMED
- Member 2: MA KHADER SHAREEF MADANI
- Member 3: SYED ATHER ALI
- Member 4: MEER HYDER SIDDIQUI
- Member 5: SHREYA TADAKALA
- Member 6: SYEDA ALIA SAMIA

---
## 💡 TAGLINE  

**“Real-Time AI/ML-Based Phishing Detection and Prevention System – Detect ✅ | Prevent ⚠ | Educate 💡”**

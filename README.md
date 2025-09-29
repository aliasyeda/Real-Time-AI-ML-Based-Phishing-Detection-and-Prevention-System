# 🛡️ Phishing Shield  

**Smart India Hackathon 2024**  
**Problem Statement: Real-Time AI/ML-Based Phishing Detection and Prevention System (PS #25159)**  

---

## 📌 OVERVIEW  
Phishing attacks are one of the most common cyber threats.  
**Phishing Shield** is a **real-time AI/ML phishing detection and prevention system** built as a **Streamlit web application**.  

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

Real-Time AI/ML-Based Phishing Detection and Prevention System/
├── app.py # Streamlit App
├── phishing_combined_model.pkl # Trained Logistic Regression Model
├── vectorizer_vocab.json # Lightweight TF-IDF Vocabulary
├── phishing_model_training.ipynb # Training Notebook
├── requirements.txt # Dependencies
├── sample_safe_email.txt # Demo (Safe Email)
├── sample_phish_email.txt # Demo (Phishing Email)
└── sample_suspicious_email.txt # Demo (Suspicious Email)

## 🎯 DEMO SAMPLES  

**✅ Safe Email Example**
Your Amazon order has been shipped:
https://www.amazon.in/order

text


**🚨 Phishing Email Example**
Urgent! Your PayPal account is limited, verify here:
http://secure-login-paypai.com

text


**⚠ Suspicious Email Example**
We detected unusual activity in your account.
Please review your profile details.

text


---

## 🚀 FUTURE SCOPE  

- Gmail/Outlook integration → automatically move phishing mails to spam  
- Browser extension for **real-time URL scanning**  
- Multi-language phishing awareness training modules  
- Enterprise dashboards for monitoring phishing attempts  

---

## 👥 TEAM  

Smart India Hackathon 2025 – *Team Name*  


Member 1: ISMAIL ALI MOHAMMED
Member 2: MA KHADER SHAREEF MADANI
Member 3: SYED ATHER ALI
Member 4: MEER HYDER SIDDIQUI
Member 5: SHREYA TADAKALA
Member 6: SYEDA ALIA SAMIA

---
## 💡 TAGLINE  

**“Real-Time AI/ML-Based Phishing Detection and Prevention System – Detect ✅ | Prevent ⚠ | Educate 💡”**

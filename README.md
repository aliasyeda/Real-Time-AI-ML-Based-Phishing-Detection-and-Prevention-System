# Real-Time-AI-ML-Based-Phishing-Detection-and-Prevention-System
 Phishing Shield
Smart India Hackathon 2024
Problem Statement: Real-Time AI/ML-Based Phishing Detection and Prevention System (PS #25159)

📌 Overview
Phishing emails and malicious URLs are one of the most common cyber threats.
Our project Phishing Shield is a real-time AI/ML‑based phishing detection and prevention system that not only detects phishing attempts but also educates users to recognize them.

We built a Streamlit web application powered by a Logistic Regression model with TF‑IDF features (~99% accuracy).
The system classifies content as:

✅ Safe
⚠ Suspicious
🚨 Phishing
Unlike Gmail or VirusTotal, our system is explainable and educational:

Highlights phishing keywords.
Shows risky domains.
Displays prediction confidence scores.
Trains users with cybersecurity tips and a quiz module.
🚀 Features
AI/ML Detection

Logistic Regression on combined phishing emails + phishing URLs datasets.
Hybrid approach with whitelist rules for trusted domains (Amazon, Google, Microsoft).
Web App (Streamlit)

🛡️ Detector → Paste text/URL or upload .txt file → Detect phishing attempts
📊 Dashboard → Stats with bar chart + donut chart
💡 Awareness Quiz → Cybersecurity tips + quiz for user learning
Explainable AI

Confidence score displayed
Suspicious keywords highlighted
Fake domains flagged
UI/UX Enhancements

Light/Dark Mode toggle
Color-coded cards (Green = Safe, Yellow = Suspicious, Red = Phish)
Balloons 🎈 on safe detection
🛠️ Tech Stack
Python 3.10+
Libraries: Streamlit, scikit-learn, pandas, numpy, plotly
📂 Project Structure
app.py → Streamlit web app
phishing_combined_model.pkl → Trained ML model
vectorizer_vocab.json → TF‑IDF vocabulary (lightweight)
phishing_model_training.ipynb → Training notebook
requirements.txt → Dependencies
Sample .txt files for demo emails
🎯 Sample Demos
✅ Safe Email: “Your Amazon order has been shipped.” → Safe
🚨 Phishing Email: “Urgent! Verify account at http://secure-paypai.com” → Phish
⚠ Suspicious Email: “Please review your profile information.” → Suspicious
🚀 Future Scope
Gmail/Outlook plugin for auto-spam filtering
Browser extension for real-time URL checks
Multi-language phishing training
Enterprise dashboard for monitoring phishing trends
👥 Team
Smart India Hackathon 2025 — CODEHEX

Member 1: ISMAIL ALI MOHAMMED
Member 2: MA KHADER SHAREEF MADANI
Member 3: SYED ATHER ALI
Member 4: MEER HYDER SIDDIQUI
Member 5: SHREYA TADAKALA
Member 6: SYEDA ALIA SAMIA

💡 Tagline
Phishing Shield – Detect ✅, Prevent ⚠, Educate 💡.

import streamlit as st
import pickle
import re
import plotly.express as px
import random

# PAGE CONFIG 
st.set_page_config(page_title="AI Phishing Detector", page_icon="🛡️", layout="wide")

# LOAD MODEL 
import pickle, json
from sklearn.feature_extraction.text import TfidfVectorizer

# Load ML model
model = pickle.load(open("phishing_combined_model.pkl", "rb"))

# Load vectorizer vocabulary (from JSON file, lightweight)
with open("vectorizer_vocab.json") as f:
    vocab = json.load(f)

# Rebuild TF-IDF vectorizer from saved vocabulary
vectorizer = TfidfVectorizer(vocabulary=vocab)

# HELPER FUNCS 
suspicious_keywords = [
    "click","urgent","password","verify","login","congratulations",
    "account","suspended","winner","bank","security","confirm","blocked"
]

def highlight_suspicious(text):
    return [w for w in suspicious_keywords if w in text.lower()]

def domain_analysis(text):
    url_pattern = r"(https?://[^\s]+)"
    urls = re.findall(url_pattern, text.lower())
    flagged = []
    for u in urls:
        if any(keyword in u for keyword in ["login","secure","verify"]):
            if not any(safe in u for safe in ["microsoft.com","amazon","google","apple.com","bankofindia.co.in"]):
                flagged.append(u)
    return urls, flagged

def predict_text(text):
    features = vectorizer.transform([text])
    proba = model.predict_proba(features)[0]
    phishing_prob = proba[1]*100
    safe_prob = proba[0]*100
    
    # === Trusted whitelist ===
    trusted_domains = ["amazon.com","amazon.in","apple.com","microsoft.com","google.com","bankofindia.co.in"]
    for domain in trusted_domains:
        if domain in text.lower():
            return "safe", phishing_prob, safe_prob + 20

    # === ML thresholds ===
    if phishing_prob >= 75:
        label = "phishing"
    elif phishing_prob >= 45:
        label = "suspicious"
    else:
        label = "safe"

    return label, phishing_prob, safe_prob

#  SESSION STATE 
if "history" not in st.session_state:
    st.session_state["history"] = {"phishing":0, "suspicious":0, "safe":0}

#  SIDEBAR 


st.sidebar.image("https://img.icons8.com/color/96/000000/security-checked.png", width=120)
st.sidebar.markdown("### 🧭 App Navigation")

menu = st.sidebar.radio(
    "",
    ["🛡️ Detector", "📊 Dashboard", "💡 Awareness & Quiz"]
)

theme_choice = st.sidebar.radio("🎨 Theme Mode:", ["🌞 Light Mode","🌙 Dark Mode"])

# LIGHT MODE 
if theme_choice == "🌞 Light Mode":
    st.markdown("""
        <style>
        .stApp {
            background: linear-gradient(to bottom right, #f5f7fa, #cfd9df);
        }

        /* Sidebar background */
        section[data-testid="stSidebar"] {
            background-color: #1a237e;
        }
        /* Header in Light Mode */
        header[data-testid="stHeader"] {
            background-color: #1a237e !important;  /* match sidebar */
            color: white !important;

}
        section[data-testid="stSidebar"] * {
            color: white !important;
        }

        /* Ensure sidebar toggle icon is always visible */
        button[kind="icon"] svg,
        button[kind="icon"] svg path,
        div[data-testid="stSidebarNav"] button[kind="icon"] svg,
        div[data-testid="stSidebarNav"] button[kind="icon"] svg path,
        section[data-testid="stSidebar"] button[kind="icon"] svg,
        section[data-testid="stSidebar"] button[kind="icon"] svg path,
        header button[kind="icon"] svg,
        header button[kind="icon"] svg path {
            fill: white !important;
            stroke: white !important;
            color: white !important;
}

        button[kind="icon"] {
            z-index: 9999 !important;
            position: relative !important;
}


        /* Force navigation text to white always */
        section[data-testid="stSidebar"] div, 
        section[data-testid="stSidebar"] label, 
        section[data-testid="stSidebar"] span,
        section[data-testid="stSidebar"] p {
            color: white !important;
        }

        /* Buttons */
        div.stButton > button {
            background: #4285F4;
            color: white !important;
            border: none;
            border-radius: 8px;
            padding: 0.6em 1.2em;
            font-weight: bold;
        }
        div.stButton > button:hover {
            background: #34A853;  /* Green hover */
            color: white !important;
        }

        /* Inputs */
        div[data-testid="stTextInput"] input {
            background-color: #ffffff;
            border: 2px solid #1a237e;
            border-radius: 6px;
            color: black !important;
        }
        div[data-testid="stFileUploader"] section {
            background-color: #ffffff;
            border: 2px dashed #1a237e;
            border-radius: 6px;
            color: black !important;
        }

        /* Normal text in Light Mode (black) */
        .stMarkdown, .stText, p, div, span, label {
            color: black !important;
        }
        </style>
    """, unsafe_allow_html=True)

# DARK MODE 
elif theme_choice == "🌙 Dark Mode":
    st.markdown("""
        <style>
        .stApp {
            background: linear-gradient(to bottom right, #0f2027, #203a43, #2c5364);
        }

        /* Sidebar background */
        section[data-testid="stSidebar"] {
            background-color: #111827;
        }
        /* Header in Dark Mode */
        header[data-testid="stHeader"] {
            background-color: #111827 !important;  /* match sidebar */
            color: white !important;
}
        section[data-testid="stSidebar"] * {
            color: white !important;
        }

      /* Ensure sidebar toggle icon is always visible  */
               
        button[kind="icon"] svg,
        button[kind="icon"] svg path,
        div[data-testid="stSidebarNav"] button[kind="icon"] svg,
        div[data-testid="stSidebarNav"] button[kind="icon"] svg path,
        section[data-testid="stSidebar"] button[kind="icon"] svg,
        section[data-testid="stSidebar"] button[kind="icon"] svg path,
        header button[kind="icon"] svg,
        header button[kind="icon"] svg path {
            fill: white !important;
            stroke: white !important;
            color: white !important;
}

        button[kind="icon"] {
            z-index: 9999 !important;
            position: relative !important;
}

        /* Force navigation text to white always */
        section[data-testid="stSidebar"] div, 
        section[data-testid="stSidebar"] label, 
        section[data-testid="stSidebar"] span,
        section[data-testid="stSidebar"] p {
            color: white !important;
        }

        /* Buttons */
        div.stButton > button {
            background: linear-gradient(135deg, #6a11cb 0%, #2575fc 100%);
            color: white !important;
            border: none;
            border-radius: 8px;
            padding: 0.6em 1.2em;
            font-weight: bold;
        }
        div.stButton > button:hover {
            background: linear-gradient(135deg, #ff416c 0%, #ff4b2b 100%);
            color: white !important;
        }

        /* Inputs */
        div[data-testid="stTextInput"] input {
            background-color: #1f2937;
            border: 2px solid #4b5563;
            border-radius: 6px;
            color: white !important;
        }
        div[data-testid="stFileUploader"] section {
            background-color: #1f2937;
            border: 2px dashed #4b5563;
            border-radius: 6px;
            color: white !important;
        }

        /* Normal text in Dark Mode (white) */
        .stMarkdown, .stText, p, div, span, label {
            color: white !important;
        }
        </style>
    """, unsafe_allow_html=True)
            


# ======================== PAGE 1: DETECTOR ===================
if menu=="🛡️ Detector":
    st.markdown("<h1 style='text-align:center;color:#1a73e8;'>🛡️ Real-Time Phishing Detection & Prevention</h1>", unsafe_allow_html=True)

    user_input = st.text_area("✍️ Paste any email text or URL:")

    uploaded = st.file_uploader("📂 Or upload a .txt email file:", type=["txt"])
    if uploaded:
        user_input = uploaded.read().decode("utf-8")
        st.info("📄 File uploaded! Preview:")
        st.code(user_input[:400] + ("..." if len(user_input)>400 else ""), language="text")

    if st.button("🔍 Run Detection"):
        if user_input.strip():
            label, phishing_prob, safe_prob = predict_text(user_input)
            st.session_state["history"][label]+=1

            if label=="phishing":
                st.markdown(f"""
                    <div style="padding:20px;border-radius:10px;
                    background: linear-gradient(135deg, #ff9a9e 0%, #f6416c 100%);
                    color:white; font-size:20px;font-weight:bold;">
                    🚨 PHISHING DETECTED 🚨<br>
                    Phishing Probability: {phishing_prob:.2f}%<br>
                    Safe Probability: {safe_prob:.2f}%<br>
                    ⚠ Access Blocked!
                    </div>
                """,unsafe_allow_html=True)

            elif label=="suspicious":
                st.markdown(f"""
                    <div style="padding:20px;border-radius:10px;
                    background: linear-gradient(135deg, #ffe066 0%, #f6d365 100%);
                    font-size:20px;font-weight:bold;">
                    ⚠️ SUSPICIOUS CONTENT ⚠️<br>
                    Phishing Probability: {phishing_prob:.2f}%<br>
                    Safe Probability: {safe_prob:.2f}%<br>
                    Recommendation: Double-check before clicking links.
                    </div>
                """,unsafe_allow_html=True)

            else:
                st.markdown(f"""
                    <div style="padding:20px;border-radius:10px;
                    background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
                    color:black; font-size:20px;font-weight:bold;">
                    ✅ SAFE EMAIL/URL ✅<br>
                    Safe Probability: {safe_prob:.2f}%<br>
                    Phishing Probability: {phishing_prob:.2f}%
                    </div>
                """,unsafe_allow_html=True)
                st.balloons()   # 🎈 animation for Safe

            # Explanations
            words = highlight_suspicious(user_input)
            if words:
                st.warning("⚠️ Suspicious Keywords: " + ", ".join(words))
            urls, flagged = domain_analysis(user_input)
            if urls:
                st.subheader("🔗 URL Analysis")
                for u in urls:
                    if u in flagged:
                        st.error(f"{u} → 🚨 Suspicious/Fake Domain")
                    else:
                        st.success(f"{u} → ✅ Trusted Domain")
        else:
            st.warning("⚠️ Please enter text or upload a file.")

# ======================== PAGE 2: DASHBOARD ==================
elif menu=="📊 Dashboard":
    st.markdown("<h1 style='color:#34a853;'>📊 Detection Dashboard</h1>", unsafe_allow_html=True)

    total = sum(st.session_state["history"].values())
    if total==0:
        st.info("No scans yet. Run the Detector first.")
    else:
        col1, col2, col3 = st.columns(3)
        col1.metric("🚨 Phishing", st.session_state["history"]["phishing"])
        col2.metric("⚠️ Suspicious", st.session_state["history"]["suspicious"])
        col3.metric("✅ Safe", st.session_state["history"]["safe"])

        # Donut Chart
        data = st.session_state["history"]
        labels = [k for k,v in data.items() if v>0]
        values = [v for v in data.values() if v>0]

        fig = px.pie(
            values=values, names=labels, hole=0.4,
            color=labels,
            color_discrete_map={"phishing":"red","suspicious":"orange","safe":"green"}
        )
        fig.update_traces(textinfo="label+percent", textfont_size=14)
        st.plotly_chart(fig)

        # Bar Chart
        st.bar_chart(data)

# ======================== PAGE 3: QUIZ =======================
elif menu=="💡 Awareness & Quiz":
    st.markdown("<h1 style='color:#ff8800;'>💡 Phishing Awareness & Quiz</h1>", unsafe_allow_html=True)

    st.subheader("✅ Safety Tips")
    st.markdown("""
    - 🕵️ Verify sender email carefully.  
    - 🌐 Hover links before clicking.  
    - 🚨 Ignore urgency-based scams.  
    - 🔐 Never share OTPs/passwords.  
    - ✅ Type official sites manually.  
    """)

    st.subheader("🎮 Awareness Quiz (5 questions)")

    # Question Bank
    question_bank = [
        {"q":"📧 'Your PayPal account is limited, click to verify.'","options":["Legit","Phishing"],"answer":"Phishing"},
        {"q":"🌐 Domain `amazon-verification.net`","options":["Safe","Phishing"],"answer":"Phishing"},
        {"q":"🎁 'Congratulations! You won a lottery.'","options":["Safe","Phishing"],"answer":"Phishing"},
        {"q":"📧 From `support@apple.com` reset password","options":["Safe","Phishing"],"answer":"Safe"},
        {"q":"🌐 Link: https://www.bankofindia.co.in/account/login","options":["Safe","Phishing"],"answer":"Safe"},
        {"q":"📧 'Urgent! Verify account now or blocked'","options":["Safe","Phishing"],"answer":"Phishing"},
        {"q":"📧 'Work from home, earn $1000 daily!'","options":["Safe","Phishing"],"answer":"Phishing"}
    ]

    quiz_questions = random.sample(question_bank, 5)
    score = 0

    for i, q in enumerate(quiz_questions):
        user_answer = st.radio(q["q"], q["options"], key=f"quiz_q{i}")
        if user_answer == q["answer"]:
            st.success("✅ Correct!")
            score += 1
        elif user_answer:
            st.error("❌ Incorrect.")

    st.subheader(f"🏆 Final Score: {score}/5")
    if score == 5:
        st.balloons()
        st.success("🎉 Excellent! You’re phishing-proof!")
    elif score >= 3:
        st.success("👍 Good job! Stay cautious.")
    else:
        st.warning("⚠️ Needs improvement. Be careful with emails.")
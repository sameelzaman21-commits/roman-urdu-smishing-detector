import pickle
import streamlit as st

st.set_page_config(page_title="Roman Urdu Scam Detector", page_icon="🛡️")
st.title("🛡️ Roman Urdu AI Scam Detector")
st.subheader("By Syed Sameel | Nixor College | 93.75% Accurate")

@st.cache_resource
def load_model():
    with open('roman_urdu_scam_model.pkl','rb') as f:
        model = pickle.load(f)
    with open('roman_urdu_vectorizer.pkl','rb') as f:
        vec = pickle.load(f)
    return model, vec

model, vectorizer = load_model()

msg = st.text_area("Type Roman Urdu SMS:", height=100, placeholder="Bhai apka easypaisa account block...")
if st.button("DETECT"):
    if msg.strip()=="":
        st.warning("Type a message first")
    else:
        v = vectorizer.transform([msg.lower()])
        pred = model.predict(v)[0]
        prob = model.predict_proba(v).max()
        if pred==1:
            st.error(f"🔴 SCAM {prob:.0%} - Delete & Report!")
        else:
            st.success(f"🟢 HAM SAFE {prob:.0%} - Safe")

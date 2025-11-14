import streamlit as st
import joblib
import re
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')
stop = set(stopwords.words('english'))

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'<.*?>', ' ', text)
    text = re.sub(r'[^a-z]', ' ', text)
    words = [w for w in text.split() if w not in stop]
    return ' '.join(words)

try:
    model = joblib.load("ReviewSentiment.joblib")
    model_ready = True
except Exception as e:
    model_ready = False
    st.error(f"Failed to load model: {e}")

def predict_sentiment(text):
    clean = preprocess_text(text)
    pred = model.predict([clean])[0]

    if pred == "positive":
        return "Positive 😊", "#2ecc71" 
    elif pred == "negative":
        return "Negative 😞", "#e74c3c" 
    else:
        return "Neutral 😐", "#95a5a6"

st.set_page_config(page_title="Spotify App Reviews Sentiment", page_icon="🎧")
st.title("🎧 Spotify App Reviews Sentiment Analysis")
st.write("Analyze user reviews to detect whether the sentiment is **positive**, **negative**, or **neutral**!")

st.divider()

user_input = st.text_area("💬 Type a Spotify review:")

if st.button("🔍 Predict"):
    if not model_ready:
        st.error("The model is not ready. Please check if 'ReviewSentiment.joblib' is in the same folder.")
    elif user_input.strip():
        hasil, warna = predict_sentiment(user_input)
        st.markdown(
            f"""
            <div style="background-color:{warna};padding:15px;border-radius:10px;color:white;text-align:center;">
                <strong>Sentiment:</strong> {hasil}
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.warning("Please enter a review first.")

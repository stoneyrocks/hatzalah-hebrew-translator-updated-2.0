import streamlit as st
import json

# Load dictionary from file
with open("terms_dict.json", "r", encoding="utf-8") as f:
    terms = json.load(f)

# Create reverse dictionary for Hebrew to English
reverse_terms = {v: k for k, v in terms.items()}

st.title("🚑 English ↔ Hebrew Medical Translator")

sentence = st.text_input("Enter a sentence in English or Hebrew:")

if sentence:
    words = sentence.strip().lower().split()
    translations = {}

    for word in words:
        # Try English to Hebrew
        result = terms.get(word.title())
        # If not found, try Hebrew to English
        if not result:
            result = reverse_terms.get(word)
        if result:
            translations[word] = result

    if translations:
        st.write("### Translations found:")
        for w, tr in translations.items():
            st.write(f"**{w}** → {tr}")
    else:
        st.error("❌ No translations found for any word.")

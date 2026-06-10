import os
import streamlit as st
from google import genai

# 1. Pastikan API Key aman dan Client didefinisikan dulu!
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    st.error("GEMINI_API_KEY belum dikonfigurasi di Secrets!")
    st.stop()

# Membuat objek client (ini yang tadi hilang/belum didefinisikan)
client = genai.Client(api_key=api_key)

# 2. Bungkus proses generate ke dalam fungsi agar bisa dipanggil oleh app.py
def get_response(msg, pickup):
    # Gabungkan pesan atau buat prompt sesuai kebutuhan aplikasi Bajaj kamu
    prompt = f"User bertanya: {msg}. Lokasi pickup: {pickup}"
    
    # Baru panggil client.models di dalam fungsi ini
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    
    return response.text
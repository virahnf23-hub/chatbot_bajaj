import os
import streamlit as st
from google import genai

# 1. Inisialisasi API Key dan Client
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    st.error("Waduh! GEMINI_API_KEY belum dipasang di Secrets Streamlit Cloud.")
    st.stop()

client = genai.Client(api_key=api_key)

# 2. Fungsi untuk mengambil respons dari Gemini
def get_response(msg, pickup):
    # Validasi: Jika input kosong atau hanya berisi spasi, jangan kirim ke API
    if not msg or str(msg).strip() == "":
        return "Halo! Silakan tulis pertanyaan Anda terlebih dahulu tentang Bajaj Semarang."

    # Menyusun prompt menjadi string murni yang jelas
    prompt = f"Pengguna bertanya tentang Bajaj di Semarang: '{str(msg)}'. Lokasi penjemputan mereka saat ini di: '{str(pickup)}'. Tolong berikan jawaban yang ramah dan membantu."
    
    try:
        # Panggil API Gemini dengan model stabil versi terbaru
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        
        # Kembalikan teks hasil dari model
        if response and response.text:
            return response.text
        else:
            return "Maaf, sistem tidak berhasil menghasilkan jawaban. Silakan coba lagi."
            
    except Exception as e:
        # Jika masih ada error dari sisi Google, tangkap di sini agar aplikasi tidak crash berwarna pink
        return f"Aplikasi mengalami kendala teknis saat menghubungi AI. (Detail: {str(e)})"
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def get_response(message, pickup=""):

    prompt = f"""
    Kamu adalah chatbot resmi Bajaj Semarang.

    Informasi:
    - Tarif antar jemput mulai Rp15.000
    - City Tour Rp75.000/jam
    - Operasional 06.00–22.00 WIB
    - Area layanan Kota Semarang
    - Lokasi penjemputan: {pickup}

    Pertanyaan pelanggan:
    {message}

    Jawab dengan ramah dan singkat.
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text
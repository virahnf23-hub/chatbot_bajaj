# Coba ganti bagian model menjadi seperti ini:
response = client.models.generate_content(
    model="gemini-2.5-flash", # Pastikan tulisannya persis seperti ini
    contents=prompt
)
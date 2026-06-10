def get_response(message, pickup=""):

    msg = message.lower()

    if "tarif" in msg:
        return f"💰 Tarif Bajaj mulai Rp15.000 dari lokasi {pickup}."

    elif "city tour" in msg:
        return "🏛️ City Tour tersedia mulai Rp75.000 per jam."

    elif "operasional" in msg:
        return "🕐 Operasional setiap hari pukul 06.00–22.00 WIB."

    elif "area" in msg:
        return "📍 Melayani seluruh wilayah Kota Semarang."

    return "🤖 Maaf, saya belum memahami pertanyaan Anda."
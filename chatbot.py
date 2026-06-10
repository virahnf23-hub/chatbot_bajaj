def get_response(message, pickup=""):

    msg = message.lower()

    if "pesan" in msg or "booking" in msg:
        return f"🛺 Bajaj siap menjemput Anda di {pickup}. Silakan tunggu konfirmasi dari admin."

    elif "tarif" in msg:
        return f"💰 Tarif mulai Rp15.000. Penjemputan dari {pickup} akan disesuaikan dengan jarak tujuan."

    elif "city tour" in msg or "wisata" in msg:
        return f"🏛️ City Tour tersedia. Penjemputan dapat dilakukan di {pickup}."

    elif "area" in msg:
        return "📍 Kami melayani seluruh wilayah Kota Semarang."

    elif "jam" in msg:
        return "🕐 Operasional setiap hari pukul 06.00–22.00 WIB."

    else:
        return "🤖 Maaf, saya belum memahami pertanyaan Anda."
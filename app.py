import streamlit as st
from chatbot import get_response

st.set_page_config(
    page_title="Bajaj Semarang",
    page_icon="🛺",
    layout="wide"
)

st.title("🛺 BAJAJ SEMARANG")
st.write("Transportasi Kota & City Tour Semarang")

menu = st.sidebar.selectbox(
    "Menu",
    ["Beranda", "Chatbot", "Booking", "Login Admin"]
)

# ==========================
# BERANDA
# ==========================
if menu == "Beranda":

    st.header("Selamat Datang")

    st.write("""
    Layanan Bajaj Semarang:

    - 🚖 Antar Jemput
    - 🏛️ City Tour
    - 💰 Tarif Mulai Rp15.000
    - 🕐 Operasional 06.00–22.00 WIB
    """)


# ==========================
# CHATBOT
# ==========================
elif menu == "Chatbot":

    st.header("🤖 Chatbot Bajaj Semarang")

    pickup = st.selectbox(
        "Lokasi Penjemputan",
        [
            "Simpang Lima",
            "Kota Lama",
            "Lawang Sewu",
            "Tugu Muda",
            "Bandara Ahmad Yani",
            "Stasiun Tawang",
            "Stasiun Poncol"
        ]
    )

    msg = st.text_input("Tulis pertanyaan")

    if st.button("Kirim"):

        response = get_response(msg, pickup)

        st.success(response)


# ==========================
# BOOKING
# ==========================
elif menu == "Booking":

    st.header("🛺 Booking Bajaj")

    nama = st.text_input("Nama")

    no_hp = st.text_input("No HP")

    lokasi = st.selectbox(
        "Lokasi Penjemputan",
        [
            "Simpang Lima",
            "Kota Lama",
            "Lawang Sewu",
            "Bandara Ahmad Yani",
            "Stasiun Tawang"
        ]
    )

    tujuan = st.text_input("Tujuan")

    layanan = st.selectbox(
        "Layanan",
        ["Antar Jemput", "City Tour"]
    )

    tanggal = st.date_input("Tanggal")

    catatan = st.text_area("Catatan")

    if st.button("Pesan Bajaj"):

        tarif = 75000 if layanan == "City Tour" else 15000

        st.success("✅ Booking Berhasil")

        st.write("### Detail Booking")

        st.write("Nama :", nama)
        st.write("No HP :", no_hp)
        st.write("Jemput :", lokasi)
        st.write("Tujuan :", tujuan)
        st.write("Layanan :", layanan)
        st.write("Tanggal :", tanggal)
        st.write("Catatan :", catatan)
        st.write("Tarif :", f"Rp {tarif:,}")

        st.info("💳 Pembayaran dilakukan kepada driver saat penjemputan.")


# ==========================
# LOGIN ADMIN
# ==========================
elif menu == "Login Admin":

    st.header("🔐 Login Admin")

    username = st.text_input("Username")

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Login"):

        if username == "admin" and password == "admin":

            st.success("Login berhasil")

        else:

            st.error("Username atau password salah")
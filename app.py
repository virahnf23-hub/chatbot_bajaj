from flask import Flask, render_template, request, jsonify, redirect, session
from flask_mysqldb import MySQL
from chatbot import get_response

app = Flask(__name__)
app.secret_key = 'bajajsemarang'

# ==========================
# KONFIGURASI DATABASE
# ==========================
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'bajajbot'

mysql = MySQL(app)

# ==========================
# HALAMAN UTAMA
# ==========================
@app.route('/')
def index():
    return render_template('index.html')


# ==========================
# CHATBOT
# ==========================
@app.route('/chat')
def chat():
    return render_template('chat.html')


@app.route('/get_response', methods=['POST'])
def response():

    data = request.get_json()

    pickup = data.get('pickup', '')
    user_message = data['message']

    bot_response = get_response(user_message, pickup)

    return jsonify({
        'response': bot_response
    })

    mysql.connection.commit()
    cur.close()

    return jsonify({
        'response': bot_response
    })


# ==========================
# BOOKING BAJAJ
# ==========================
@app.route('/booking', methods=['GET', 'POST'])
def booking():

    if request.method == 'POST':

        nama = request.form['nama']
        no_hp = request.form['no_hp']
        lokasi = request.form['lokasi_jemput']
        tujuan = request.form['tujuan']
        layanan = request.form['layanan']
        tanggal = request.form['tanggal']
        catatan = request.form['catatan']

        # Hitung tarif
        if layanan == "City Tour":
            tarif = 75000
        else:
            tarif = 15000

        status = "Menunggu Driver"

        cur = mysql.connection.cursor()

        cur.execute(
            """
            INSERT INTO booking
            (nama, no_hp, motor, tanggal, keluhan)
            VALUES (%s,%s,%s,%s,%s)
            """,
            (
                nama,
                no_hp,
                layanan,
                tanggal,
                f"Jemput: {lokasi} | Tujuan: {tujuan} | Catatan: {catatan}"
            )
        )

        mysql.connection.commit()

        booking_id = cur.lastrowid

        cur.close()

        return render_template(
            'booking_success.html',
            booking_id=booking_id,
            nama=nama,
            lokasi=lokasi,
            tujuan=tujuan,
            layanan=layanan,
            tarif=tarif,
            status=status
        )

    return render_template('booking.html')


# ==========================
# LOGIN ADMIN
# ==========================
@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']

        cur = mysql.connection.cursor()

        cur.execute(
            """
            SELECT *
            FROM admin
            WHERE username=%s
            AND password=%s
            """,
            (username, password)
        )

        admin = cur.fetchone()

        cur.close()

        if admin:

            session['admin'] = username

            return redirect('/dashboard')

        return render_template(
            'login.html',
            error='Username atau password salah.'
        )

    return render_template('login.html')


# ==========================
# DASHBOARD ADMIN
# ==========================
@app.route('/dashboard')
def dashboard():

    if 'admin' not in session:

        return redirect('/login')

    cur = mysql.connection.cursor()

    cur.execute("""
        SELECT *
        FROM booking
        ORDER BY id DESC
    """)

    booking = cur.fetchall()

    cur.close()

    return render_template(
        'dashboard.html',
        booking=booking
    )


# ==========================
# LOGOUT
# ==========================
@app.route('/logout')
def logout():

    session.clear()

    return redirect('/')


# ==========================
# JALANKAN APLIKASI
# ==========================
if __name__ == '__main__':
    app.run(debug=True)

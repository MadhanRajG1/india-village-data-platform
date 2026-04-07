from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)

# 🔌 MySQL connection
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Madhanmaddy_144",  # 👈 change this
        database="india_data"
    )

# 🟡 1. Get all states
@app.route('/states', methods=['GET'])
def get_states():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT DISTINCT State FROM villages")
    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify([i[0] for i in data])


# 🟡 2. Get districts
@app.route('/districts', methods=['GET'])
def get_districts():
    state = request.args.get('state')

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT DISTINCT District FROM villages WHERE State=%s", (state,))
    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify([i[0] for i in data])


# 🟡 3. Get subdistricts
@app.route('/subdistricts', methods=['GET'])
def get_subdistricts():
    district = request.args.get('district')

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT DISTINCT SubDistrict FROM villages WHERE District=%s", (district,))
    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify([i[0] for i in data])


# 🟡 4. Get villages
@app.route('/villages', methods=['GET'])
def get_villages():
    subdistrict = request.args.get('subdistrict')

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT Village FROM villages WHERE SubDistrict=%s LIMIT 100", (subdistrict,))
    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify([i[0] for i in data])


# ▶️ Run server
if __name__ == '__main__':
    app.run(debug=True)
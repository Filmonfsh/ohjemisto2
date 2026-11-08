import mysql.connector
from flask import Flask

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='filmon',
    autocommit=True
)

app = Flask(__name__)

@app.route('/kenttä/<icao>')
def kenttä(icao):
    sql = "SELECT name, municipality FROM airport WHERE ident = %s"
    kursori = yhteys.cursor()
    kursori.execute(sql, (icao,))
    tulos = kursori.fetchone()

    vastaus = {
        "ICAO": icao,
        "Name": tulos[0],
        "Municipality": tulos[1]
    }
    return vastaus

app.run(host='127.0.0.1', port=3000)
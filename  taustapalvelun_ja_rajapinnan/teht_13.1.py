from flask import Flask

app = Flask(__name__)

@app.route('/alkuluku/<luku>')
def alkuluku(luku):
    luku = int(luku)

    on_alkuluku = True
    if luku < 2:
        on_alkuluku = False

    for i in range(2, luku):
        if luku % i == 0:
            on_alkuluku = False

    vastaus = {
        "Number": luku,
        "isPrime": on_alkuluku
    }
    return vastaus

app.run(host='127.0.0.1', port=3000)
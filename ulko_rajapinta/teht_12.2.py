import requests

avain = "736093d84732fbcb2999829b14026a0e"

paikkakunta = input("Anna paikkakunta: ")

pyyntö = "https://api.openweathermap.org/data/2.5/weather?q=" + paikkakunta + "&appid=" + avain + "&lang=fi"
vastaus = requests.get(pyyntö).json()

säätila = vastaus["weather"][0]["description"]
celsius = vastaus["main"]["temp"] - 273.15

print("Säätila:", säätila)
print("Lämpötila:", round(celsius, 1), "°C")
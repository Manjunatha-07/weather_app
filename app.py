from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)

API_KEY = "458dd518ce5f20bf5e7d3ad21439208c"

@app.route('/', methods=['GET', 'POST'])
def home():
    weather = None

    if request.method == 'POST':
        city = request.form['city']
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        
        response = requests.get(url)
        data = response.json()

        if data["cod"] == 200:
            weather = {
                "city": city,
                "temp": data["main"]["temp"],
                "desc": data["weather"][0]["description"],
                "humidity": data["main"]["humidity"]
            }

    return render_template('home.html', weather=weather)


port = int(os.environ.get("PORT", 5000))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port)

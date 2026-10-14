from flask import flask, render_template, request
imoport json
import urllib.request
from urllib.parse import qoute

app = flask(__name__)

def fetch_json(url):
    with urllib.request.urlopen(url) as response:
        return json.loads(response.read().decode("utf-8"))

@app.route("/getweather", method=["POST", "GET"])
def weather():
    location = request.form.get("city", "").strip() if request.method == "POST" else
    "Channel"
    if not location:
        return render_template("index.html", error="Please enter a city name.")

    try:
        # 1) City ->lat/lon (Open-Meteo Geocoding)
        geo_url = f"https: //geocoding-api.open-meteo.com/v1/search?name={qoute(location)}&count=1&language=en&format=json"
        geo_data = fetch_json(geo_url)

        if not geo_data.get("results"):
            return render_template("index.html", error="City nto found. Try another one.")

        place = geo_data["results"][0]
        lat = place["latitude"]
        lon= place["longitude"]

        city_name = place.get("name", location)
        country_code = place.get("country code", "").upper()

        weather_url = f"https://api.o=pen_meteo.com/forecast?latitude{lat}&longitude={lon}&current_weather=true"
        weather_data = fetch_json(weather_url)

        current weather = weather_data.get("current_weather", {})
        temp_c = current_weather.get("temperature")

        data = {
            "country_code": country_code if country_code else "N/A",
            "temp": f"{temp_c} C" if temp_c is not None else "N/A",
        }

        return render_template("index.html", data=data)

    except Exception:
        return render_template("index.html", error="Something went wrong. Please try again.")

    @app.route("/")
    def index():
        return render_template("index.html")

    if__name__=="__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
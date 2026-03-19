from flask import Flask, render_template, request
from datetime import datetime
from fetcher import get_matches_by_city
from config import CITY_TEAMS

app = Flask(__name__)

ALL_CITIES = sorted(CITY_TEAMS.keys())


@app.route("/", methods=["GET"])
def index():
    current_month = datetime.now().strftime("%Y-%m")
    return render_template("index.html", cities=ALL_CITIES,
                           current_month=current_month, matches=None, error=None)


@app.route("/fetch", methods=["POST"])
def fetch():
    month = request.form.get("month", "").strip()
    selected_cities = request.form.getlist("cities")

    error = None
    matches = None
    grouped = {}

    try:
        if not month:
            month = datetime.now().strftime("%Y-%m")
        datetime.strptime(month, "%Y-%m")

        cities_filter = selected_cities if selected_cities else None
        matches = get_matches_by_city(month, cities_filter)

        for m in matches:
            grouped.setdefault(m["city"], []).append(m)

    except ValueError as e:
        error = str(e)

    return render_template("index.html", cities=ALL_CITIES,
                           current_month=month,
                           selected_cities=selected_cities,
                           grouped=grouped,
                           total=len(matches) if matches else 0,
                           month=month,
                           error=error)


if __name__ == "__main__":
    import webbrowser
    webbrowser.open("http://127.0.0.1:5000")
    app.run(debug=False)

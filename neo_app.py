import requests
from flask import Flask, render_template, request

app= Flask(__name__,template_folder=".")
NASA_API_KEY= "rP9GQchQwMPpwrnphb7q8qLqHFPC77zw9WDnNWF6"

@app.route('/')
def home():
    return render_template('index.html',searched=False)

@app.route('/track', methods=['POST'])
def track_asteroids():
    start_date = request.form['start_date']
    end_date = request.form['end_date']
    asteroids = get_asteroid_data(start_date, end_date)
    return render_template('index.html', asteroids=asteroids, searched=True)

def get_asteroid_data(start_date, end_date):
    url=f"https://api.nasa.gov/neo/rest/v1/feed?start_date={start_date}&end_date={end_date}&api_key={NASA_API_KEY}"
    response = requests.get(url)
    all_asteroids=[]

    if response.status_code==200:
        data=response.json()
        for date_key in data['near_earth_objects']:
            for asteroid in data['near_earth_objects'][date_key]:
                all_asteroids.append(asteroid)
    return all_asteroids

if(__name__=="__main__"):
    app.run(debug=True)



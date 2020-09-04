from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
from scrape_mars import scrape

app = Flask(__name__)
mongo =  PyMongo(app, uri="mongodb://localhost:27017/planets")


@app.route("/")
def index():
    planet_data = mongo.planets.Mars.find_one()
    return render_template("index.html", planet_data=planet_data)

@app.route("/scrape")
def scraper():
    planets = mongo.planets.Mars
    planet_data = scrape()
    planets.update({}, planet_data, upsert=True)
    return redirect("/", code=302)




























if __name__ == "__main__":
    app.run()
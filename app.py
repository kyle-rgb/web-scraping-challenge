from flask import Flask, render_template, redirect
from scrape_mars import scrape

@app.route("/")
def index():


@app.route("/scrape")
def scraper():
    planets = mongo.db.planets
    planets_data = scrape()
    planets.update({}, planets_data, upsert=True)
    return redirect("/", code=302)




























if __name__ == "__main__":
    app.run()
from flask import Flask, render_template, redirect
import pymongo
from flask_pymongo import PyMongo
from scrape_mars import scrape

app = Flask(__name__)
conn = 'mongodb://localhost:27017'

client = pymongo.MongoClient(conn)
db = client.planets

db.mars.drop()

# Test Data
db.mars.insert_one({"Planet_News": {"title": "Article", "blurb": "blurb"}, "Planet_Facts": {"table": {"Mars": {"key": "value"}}},
                    "Planet_Image": {"featured_image_url": "https://thumbs-prod.si-cdn.com/PMYKxQ9NTtXkrcWz3tMItcFfcjs=/800x600/filters:no_upscale()/https://public-media.si-cdn.com/filer/mars_img.jpg"},
                    "Hemispheres": [{"img_url": "https://upload.wikimedia.org/wikipedia/commons/8/8a/Jupiter_family.jpg", "title": "Hemisphere"},
                    {"img_url": "https://upload.wikimedia.org/wikipedia/commons/7/7b/Io_highest_resolution_true_color.jpg", "title": "Hemisphere2"}]})

@app.route("/")
def index():
    planet_data = db.mars.find_one()
    return render_template("index.html", planet_data=planet_data)

@app.route("/scrape")
def scraper():
    planet_data = scrape()
    db.mars.update({}, planet_data, upsert=True)
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run()
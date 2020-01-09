from flask import Flask, render_template
from flask_pymongo import PyMongo
import Web-Scraping_Challenge

app = Flask(__name__)

#12.3.7 = Ins_Scrape_and_Render

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)


@app.route("/")
def index():
    scrape = mongo.db.scrape.find_one()
    return render_template("index.html", scrape=scrape)

@app.route("/scrape")
def scrape():
    scrape = mongo.db.scrape
    scrape_data = scrape_mars.scrape()
    scrape.update({}, scrape_data, upsert=True)
    return redirect("/", code=302)

if __name__ == "__main__":
    app.run()

from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
from scrape_mars import scrape_info
import scrape_mars

###############p##################################
# Flask Setup
#################################################

app = Flask(__name__)

mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_mission_app")

# #################################################
# # Flask Routes
# #################################################

@app.route("/")
def index():
    mars = mongo.db.collection.find_one()
    return render_template("index.html", mars=mars)


@app.route("/scrape_mars")
def scrape():
    mars_data = scrape_mars.scrape_info()
    mongo.db.collection.update({}, mars_data, upsert=True)
    flash('Process complete!')
    return redirect("/")
    

if __name__ == '__main__':
    app.run(debug=True)
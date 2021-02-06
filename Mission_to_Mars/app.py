from flask import Flask, render_template, redirect
from flask_pymongo import pymongo
from scrape_mars import scrape_info


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
    return render_template("index.html")


@app.route("/scrape")
def scrape():
    mars = client.db.mars
    mars_data = scrape_mars.scrape_info()
    mars.insert(mars_data)
    return redirect("/")
    

if __name__ == '__main__':
    app.run(debug=True)
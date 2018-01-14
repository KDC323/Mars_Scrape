# Dependencies
from flask import Flask, jsonify, render_template, redirect
import pymongo
import scrape_mars
from splinter import Browser
from pprint import pprint

# Flask Set up
app = Flask(__name__)



client = pymongo.MongoClient("mongodb://%s:%s@ds255797.mlab.com:55797/heroku_480tcjhm" % ("admin", "mars_blah"))
db = client.heroku_480tcjhm
collection = db.mars


@app.route("/")
def welcome():

    
    # """List all available api routes."""
    print("Retrieving homepage")


    mars_info = collection.find_one()
    print(mars_info)
   

    return render_template("index.html", dict=mars_info)
    

@app.route("/scrape")
def scrape_route():
    print('Scraping Mars data...')

    db.collection.remove()
    new_data = scrape_mars.Scrape()
    db.collection.insert_one(new_data)
    
    # data = scrape_mars.Scrape()
    # print("Scrape return:")
    # print(data)

    # # test = collection.find_one({"uniqueID":"1"})
    # # print("Find in Mongo")
    # # pprint(test)


    # collection.update(
    #     {"id":"1"},
    #     {'$set':data},
    #     upsert=True
    # )

    # print("After update")
    # test = collection.find_one({"id":"1"})
    # pprint(test)

    # print("MongoDB updated")
    # # mongod.terminate()

    return redirect("http://localhost:5000/", code=302)

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import mars_scrape

app = Flask(__name__)

app.config["MONGO_URI"] = "mongo://localhost:5000/mars_app"
mongo = PyMongo(app)

@app.route("/")
def index():
    marsdata = list(mongo.db.marsdata.find())
    print(len(marsdata))
    return render_template('index.html', marsdata=marsdata)

@app.route('/scrape')
def scraper():
    marsdata = mongo.db.marsdata
    mars_data = mars_scrape.scrape_everything()
    marsdata.update({}, mars_data, upsert=True)
    
    print(len(marsdata))
    
    return redirect('/', code=302)

if __name__ == '__main__':
    app.run(debug=True)
    
    
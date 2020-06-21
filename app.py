from flask import Flask,render_template,request,g,redirect,url_for
app = Flask(__name__)
from flask_wtf import FlaskForm
from wtforms import StringField ,SubmitField
from wtforms.validators import DataRequired, ValidationError
from tabulate import tabulate
import requests
import json, random
from flask_sqlalchemy import SQLAlchemy


from scrape import get_link_of_song, get_all_links
from check import Emotion

url = "https://deezerdevs-deezer.p.rapidapi.com/search"

era_array = ['90s' , '80s' , '70s' , '2000s' , '2010s' , 'new' , 'old' , '60s']

# default_songs_array

headers = {
    'x-rapidapi-host': "deezerdevs-deezer.p.rapidapi.com",
    'x-rapidapi-key': "1693ad990amsh3a263f5fba31c9fp1821abjsnb2534e537b6c"
    }





app.secret_key = 'fdklnklfdnlznbzklklnh '
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class band_names(db.Model):
    id = db.Column(db.Integer,primary_key= True)
    name = db.Column(db.String(160), nullable = False)


    def __repr__(self):
        return f"band_names('{self.name}')"


@app.route('/')
def home():

    return render_template("home.html" )


@app.route('/our_recommendation')
def recommendation():

    popo = (band_names.query.all() )
    popo = str(random.choice(popo))
    print(type(popo))
    popo = (popo.split('('))
    print(popo)
    popo = (popo[1].split(')'))[0]
    id = popo

    artist_link_value = (get_all_links( id ))


    return render_template("recommendation.html" , popo =  artist_link_value)



@app.route('/first_view', methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        result = request.form
        search_form_value = result['q']
        get_emotion_value = Emotion(search_form_value)
        # print(get_emotion_value)

        id = get_emotion_value
        # print("Changed")
        era_year =  random.choice(era_array)
        # print(era_year)
        id = era_year + " " + id
        # print(id)
        querystring = {"q":id}
        response = requests.request("GET", url, headers=headers, params=querystring)
        val = (response.text)
        my_dict=json.loads(val)

        a=[]
        for num in (my_dict['data']):

            title_value = ((num)['title'])
            artist_name_value = (((num)['artist'])['name'])
            artist_link_value = (get_link_of_song(title_value , artist_name_value))

            if artist_link_value is None:
                artist_link_value = ""
                print(artist_link_value)

            print("Link- ",artist_link_value)
            b= {"title_value":title_value ,"artist_link_value": artist_link_value, "artist_name_value" : artist_name_value}
            a.append(b)
        # print(a)

        return render_template("index.html", post = a)



    return render_template("get_audio.html")










@app.errorhandler(404)

def not_found(e):
  return render_template("error.html")



if __name__ == "__main__":
    app.run(debug=False)

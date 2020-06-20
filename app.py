from flask import Flask,render_template,request,g
app = Flask(__name__)
from flask_wtf import FlaskForm
from wtforms import StringField ,SubmitField
from wtforms.validators import DataRequired, ValidationError
from tabulate import tabulate
import requests
import json
from scrape import get_link_of_song
from ibm_watson import ToneAnalyzerV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


url = "https://deezerdevs-deezer.p.rapidapi.com/search"




headers = {
    'x-rapidapi-host': "deezerdevs-deezer.p.rapidapi.com",
    'x-rapidapi-key': "1693ad990amsh3a263f5fba31c9fp1821abjsnb2534e537b6c"
    }




app.secret_key = 'fdklnklfdnlznbzklklnh '


@app.route('/')
def index():
    print("Changed")
    querystring = {"q":"Chill 60s"}
    response = requests.request("GET", url, headers=headers, params=querystring)
    val = (response.text)
    my_dict=json.loads(val)


    a=[]
    for num in (my_dict['data']):

        title_value = ((num)['title'])
        artist_pic_value = (((num)['artist'])['picture_big'])
        artist_name_value = (((num)['artist'])['name'])
        artist_link_value = (get_link_of_song(title_value , artist_name_value))
        b= {"title_value":title_value , 'artist_pic_value':artist_pic_value ,"artist_link_value": artist_link_value, "artist_name_value" : artist_name_value}
        a.append(b)

    return render_template("index.html", post = a)

@app.errorhandler(404)

def not_found(e):
  return render_template("error.html")

def Emotion(id):
    authenticator = IAMAuthenticator('gShpJ1z419dIvo8i4PgG6wbq2IKpo4AoJ0TH-xzQ-hTA')
    tone_analyzer = ToneAnalyzerV3(
        version='2017-09-21',
        authenticator=authenticator
    )

    tone_analyzer.set_service_url('https://api.eu-gb.tone-analyzer.watson.cloud.ibm.com/instances/a92fa2f2-7e10-491e-bd71-2b8b96f4c32f')
    utterances = [
        {
            "text" : id ,
            "user" : "agent"
        }
    ]

    utterance_analyses = tone_analyzer.tone_chat(utterances).get_result()
    return (json.dumps(utterance_analyses, indent=2))


if __name__ == "__main__":
    app.run(debug=True)
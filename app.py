from flask import Flask,render_template,request,g,redirect,url_for
app = Flask(__name__)
from flask_wtf import FlaskForm
from wtforms import StringField ,SubmitField
from wtforms.validators import DataRequired, ValidationError
from tabulate import tabulate
import requests
import json



from scrape import get_link_of_song


url = "https://deezerdevs-deezer.p.rapidapi.com/search"




headers = {
    'x-rapidapi-host': "deezerdevs-deezer.p.rapidapi.com",
    'x-rapidapi-key': "1693ad990amsh3a263f5fba31c9fp1821abjsnb2534e537b6c"
    }





app.secret_key = 'fdklnklfdnlznbzklklnh '


@app.route('/')
def home():

    return render_template("home.html")


@app.route('/first_view', methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        result = request.form
        search_form_value = result['q']


        return redirect(('/results/'+ search_form_value ))


    return render_template("get_audio.html")






@app.route('/results/<id>',methods=['GET',"POST"])
def results(id):
    print("Changed")
    id = str(id)

    querystring = {"q":id}
    response = requests.request("GET", url, headers=headers, params=querystring)
    val = (response.text)
    my_dict=json.loads(val)


    a=[]
    for num in (my_dict['data']):

        title_value = ((num)['title'])
        artist_pic_value = (((num)['artist'])['picture_big'])
        artist_name_value = (((num)['artist'])['name'])
        artist_link_value = (get_link_of_song(title_value , artist_name_value))

        if artist_link_value is None:
            artist_link_value = ""
            print(artist_link_value)


        print("Link- ",artist_link_value)
        b= {"title_value":title_value , 'artist_pic_value':artist_pic_value ,"artist_link_value": artist_link_value, "artist_name_value" : artist_name_value}
        a.append(b)

    return render_template("index.html", post = a)

@app.errorhandler(404)

def not_found(e):
  return render_template("error.html")



if __name__ == "__main__":
    app.run(debug=True)

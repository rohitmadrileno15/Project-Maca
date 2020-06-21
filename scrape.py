import requests,string
import re
from youtube_search import YoutubeSearch

def get_link_of_song(song_title = None, singer_name = None):

    song_title = list(song_title)
    # print(song_title)
    for i in song_title:
        if(i in string.punctuation ):
            song_title.remove(i)

    song_title = "".join(song_title)
    song_title = re.sub('\s+', '+', song_title)

    singer_name = list(singer_name)
    # print(singer_name)
    for i in singer_name:
        if(i in string.punctuation ):
            singer_name.remove(i)

    singer_name = "".join(singer_name)
    singer_name = re.sub('\s+', '+', singer_name)

    # print(song_title)
    # print(singer_name)
    src_url = song_title + "+" + singer_name
    results = YoutubeSearch(src_url, max_results=10).to_dict()


    # print((results))
    c = 0
    link_of_song = ""
    for num in results:
        if(c==0):
            link_of_song = (num['link'])
            c+=1

    return link_of_song


def get_all_links(song_title = "", singer_name = ""):
    song_title = list(song_title)
    # print(song_title)
    for i in song_title:
        if(i in string.punctuation ):
            song_title.remove(i)

    song_title = "".join(song_title)
    song_title = re.sub('\s+', '+', song_title)

    singer_name = list(singer_name)
    # print(singer_name)
    for i in singer_name:
        if(i in string.punctuation ):
            singer_name.remove(i)

    singer_name = "".join(singer_name)
    singer_name = re.sub('\s+', '+', singer_name)


    src_url = song_title + "+" + singer_name
    results = YoutubeSearch(src_url, max_results=10).to_dict()

    # print((results))

    c = 0

    link_of_song = []

    for num in results:
        if(c==0):
            c+=1
            continue
        if(c<8):
            b= { "artist_link_value": num['link'] , 'title_value': num['title'] }

            link_of_song.append(b)
            c+=1

    # print(link_of_song)
    return link_of_song



print(get_all_links( "Queen"))

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
    link_of_song = None
    for num in results:
        if(c==0):
            link_of_song = (num['link'])
            c+=1

    return link_of_song



# print(get_link_of_song("Bohemian Rhapsody", "Queen"))

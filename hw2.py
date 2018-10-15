import requests
import re
import matplotlib.pyplot as plt


def lyrics_word_count_easy(artist, song, phrase):
    r = requests.get("https://api.lyrics.ovh/v1/" + artist + "/" + song)
    #print(r.json())
    try:
        if "lyrics" not in r.json():
            return -1
    except:
        pass
    song_text = r.json()["lyrics"].lower()
    return song_text.count(phrase)

def lyrics_word_count(artist, phrase):
    #Note that I included artists featured with Rick Astley...
    import os
#     api_key = os.environ.get("$MUSICMATCHAPI")
#     print(api_key)
    root = "http://api.musixmatch.com/ws/1.1/"
    params = {
        "apikey": "c326723cfb3ccfbf64a939b843042b72",
        "q_artist": artist, 
        "s_artist_rating": "desc"
    }
    phrase_count = 0
    
    #MAKE SURE THE ARTIST EXISTS!!
    r = requests.get(root + "artist.search", params = params)
    artists_list = r.json()['message']['body']['artist_list']
    if (len(artists_list) == 0):
        return -1
    artist_key_dict = {x["artist"]["artist_name"]: x["artist"]["artist_mbid"] for x in artists_list}
    if artist not in artist_key_dict:
        return -1
    
    #GET ALL THE "FEAT OTHER ARTIST" SONGS
    feat_list = [artist]
    for a in artist_key_dict.keys():
        if artist in a and "feat." in a:
            feat_list.append(a)
    
    url = "https://api.lyrics.ovh/v1/"
    #FIND ALL OF THE ARTISTS SONGS!!
    track_names = {}
    for a in feat_list:
        track_names[a] = []
        params = {
            "apikey": "c326723cfb3ccfbf64a939b843042b72",
            "q_artist": a,
            "page_size": 100,
            "s_track_rating": "desc",
        }

        r = requests.get(root + "track.search", params = params)
        track_list = r.json()['message']['body']['track_list']
        if (len(track_list) == 0):
            break
        for x in track_list:
            track_names[a].append(x["track"]["track_name"])

    song_text_count = 0
    for a in track_names.keys():
        print(track_names[a])
        if len(track_names[a]) == 0:
            continue
        for song in track_names[a]:
            r = requests.get("https://api.lyrics.ovh/v1/" + a + "/" + song)
            if "lyrics" not in r.json():
                break
            song_text = r.json()["lyrics"].lower()
            song_text_count += song_text.count(phrase)

    return song_text_count

def visualize():
    import numpy as np
    #Line graph
    x = np.array([ 0., 1., 2., 3., 4., 5., 6., 7., 8., 9.,10., 11., 12., 13., 14., 15., 16., 17., 18., 19., 20., 21., 22., 23., 24., 25., 26., 27., 28., 29.])
    y = np.array([ 0., 25., 27., 4., -22., -28., -8., 19., 29., 12., -16., -29., -16., 12., 29., 19., -8., -28., -22., 4., 27., 25., -0., -25., -27., -3., 22., 28., 8., -19.])
    line_graph = plt.subplot(2, 1, 1)
    line_graph.set_title("Line Graph")
    plt.plot(x, y)
    
    #Historgram
    hist = plt.subplot(2,2,3)
    hist.set_title("Histogram")

    hist.hist((x,y))

    #Scatter plot
    scatter = plt.subplot(2,2,4)
    scatter.set_title("Scatter")
    scatter.scatter(x, y)
    

    return plt.show()

print(lyrics_word_count("Pink Floyd", "the"))

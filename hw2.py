import requests
import re
import matplotlib.pyplot as plt


def lyrics_word_count_easy(artist, song, phrase):
    r = requests.get("https://api.lyrics.ovh/v1/" + artist + "/" + song)
    if "lyrics" not in r.json():
        return -1
    song_text = r.json()["lyrics"].lower()
    return song_text.count(phrase)

def lyrics_word_count(artist, phrase):
    pass
    
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

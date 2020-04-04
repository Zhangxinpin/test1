
import requests
import json
import pandas as pd
from tkinter import *

root = Tk()
root.geometry('900x400')
root.title('GUI_Songs')

def song_scraper():
    # establishing the base site / site to reference / pull data from
    base_site = 'https://itunes.apple.com/search'
    # building a url with parameter off the base site
    url = base_site + '?term=the+beatles&country=US'
    # checking if URL is valid
    response = requests.get(url)
    # auto incorporating parameters --> much easier
    r = requests.get(base_site, params= {'term': 'ynw melly', 'country': 'us', 'limit': 200})
    # getting the data from the url setting it equal to variable info
    info = r.json()
    # printing info keys
    #print(info.keys())
    # creating variable for data sorting using panda
    songs_df = pd.DataFrame(info['results']) 
    # printing the data table
    #print(songs_df)
    label = Label(root, text=str(songs_df))
    label.pack()

b = Button(root,text='RUN',command=song_scraper)
b.pack(side='bottom')

root.mainloop()
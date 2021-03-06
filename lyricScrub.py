import requests
import sys
from bs4 import BeautifulSoup


client_access_token = '78M46rgxDXLJrbqVPzd9kpLHBCMPrGO0sfrgCOX2oUSPEWRu9lMp2WODlncphmoQ'

LYRICS = [""]
SongFound = True


def request_song_info(song_title, artist_name):
    base_url = 'https://api.genius.com'
    headers = {'Authorization': 'Bearer ' + client_access_token}
    search_url = base_url + '/search'
    data = {'q': song_title + ' ' + artist_name}
    response = requests.get(search_url, data=data, headers=headers)

    json = response.json()
    remote_song_info = None
    for hit in json['response']['hits']:
        if artist_name.lower() in hit['result']['primary_artist']['name'].lower():
            remote_song_info = hit
            break

    # Extract lyrics from URL if song was found
    if remote_song_info:
        song_url = remote_song_info['result']['url']
        Lyrics = scrap_song_url(song_url)

        # store lyrics in a list accesible by guiDisplay
        LYRICS.append(Lyrics)

    else:
        global SongFound
        SongFound = False


def scrap_song_url(url):
    page = requests.get(url)
    html = BeautifulSoup(page.text, 'html.parser')
    lyrics = html.find('div', class_='lyrics').get_text()

    return lyrics


def lyricFind(songTitle, artistName):
    args_length = len(sys.argv)
    if args_length == 1:
        # Get info about song currently playing on Spotify
        song_title = songTitle
        artist_name = artistName
    elif args_length == 3:
        # Use input as song title and artist name
        song_info = sys.argv
        song_title, artist_name = song_info[1], song_info[2]
    else:
        LYRICS.append("Unable to find song")

    # Search for matches in request response
    request_song_info(song_title, artist_name)


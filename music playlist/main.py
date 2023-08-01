import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pprint

# date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
date = "2021-07-30"
song_url = "https://www.billboard.com/charts/hot-100/" + date

Client_ID = "aa1d712fb57a4a3a99546b08081d973e"
Client_Secret = "b64ae509c3e84bf18bf459cd5f8a35f7"

response = requests.get(url=song_url)
data = response.text
soup = BeautifulSoup(data, 'html.parser')
music_array = soup.findAll(name="span", class_="chart-element__information__song")
song_names = [song.getText() for song in music_array]
print(soup.title.text)

print(music_array)

# Spotify Authentication
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://localhost:8000",
        client_id=Client_ID,
        client_secret=Client_Secret,
        show_dialog=True,
        cache_path="token.txt"
    )
)

user_id = sp.current_user()["id"]
print(user_id)

# Searching Spotify for songs by title
song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

# Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)

# Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)

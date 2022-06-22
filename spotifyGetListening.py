# Use the Spotify API (Using Spotipy) to get the Currently playing Music.
import spotifySecret as secret
import spotipy
import os

tokenfile = "spotifyToken.txt"

while True:
    try:
        if not os.path.exists(tokenfile):
            userToken = spotipy.util.prompt_for_user_token(secret.USERNAME,
                                                           secret.SCOPE,
                                                           secret.CLIENT_ID,
                                                           secret.CLIENT_SECRET,
                                                           secret.REDIRECT_URI)
            with open(tokenfile, "w") as file:
                file.write(userToken)
        else:
            with open(tokenfile, "r") as file:
                userToken = file.readline()

        sp = spotipy.Spotify(auth=userToken)
        print("Logging in as:", sp.me()['display_name'])
        break
    except spotipy.exceptions.SpotifyException:
        print("Token Failed, Relog!")
        os.remove(tokenfile)
        continue


def nowPlaying():
    curPlay = sp.current_user_playing_track()
    artists = []
    for artist in curPlay['item']['artists']:
        artists.append(artist['name'])

    return {
        'error': False,
        'nowplaying': curPlay['is_playing'],
        'title': curPlay['item']['name'],
        'artists': artists,
        'progress': curPlay['progress_ms'],
        'length': curPlay['item']['duration_ms']
    }

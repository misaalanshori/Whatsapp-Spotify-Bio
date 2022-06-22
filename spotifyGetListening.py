# Use the Spotify API (Using Spotipy) to get the Currently playing Music.
import spotifySecret as secret
import spotipy
import os

# tokenfile = "spotifyToken.txt"


# try:
#     userToken = spotipy.util.prompt_for_user_token(secret.USERNAME,
#                                                     secret.SCOPE,
#                                                     secret.CLIENT_ID,
#                                                     secret.CLIENT_SECRET,
#                                                     secret.REDIRECT_URI)

#     sp = spotipy.Spotify(auth=userToken)
#     print("Logging in as:", sp.me()['display_name'])
# except spotipy.exceptions.SpotifyException:
#     print("Token Failed, Relog!")

try:
    sp_oauth = spotipy.oauth2.SpotifyOAuth(client_id=secret.CLIENT_ID,client_secret=secret.CLIENT_SECRET,redirect_uri=secret.REDIRECT_URI,scope=secret.SCOPE)
    token_info = sp_oauth.get_cached_token() 
    if not token_info:
        auth_url = sp_oauth.get_authorize_url()
        print(auth_url)
        response = input('Paste the above link into your browser, then paste the redirect url here: ')

        code = sp_oauth.parse_response_code(response)
        token_info = sp_oauth.get_access_token(code)

        userToken = token_info['access_token']

    sp = spotipy.Spotify(auth=userToken)
    print("Logging in as:", sp.me()['display_name'])
except spotipy.exceptions.SpotifyException:
    print("Token Failed, Relog!")

def nowPlaying():
    curPlay = sp.current_user_playing_track()
    artists = []

    if  curPlay == None or not curPlay['is_playing']:
        return {
            'error': False,
            'nowplaying': False
        }
    for artist in curPlay['item']['artists']:
        artists.append(artist['name'])

    return {
        'error': False,
        'nowplaying': curPlay['is_playing'],
        'title': curPlay['item']['name'],
        'artists': artists,
        'progress': curPlay['progress_ms']//1000,
        'length': curPlay['item']['duration_ms']//1000
    }

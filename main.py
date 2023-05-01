from flask import Flask, render_template
import spotipy
from spotipy import SpotifyClientCredentials
import os 

# Store CLIENT_ID, CLIENT_SECRET, and USERNAME 
# in the Replit Secrets tab on the left
CLIENT_ID = os.environ["CLIENT_ID"]
CLIENT_SECRET = os.environ["CLIENT_SECRET"]
USERNAME = os.environ["USERNAME"]

auth_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)

# Create sp, the spotipy Spotify client 
sp = spotipy.Spotify(client_credentials_manager=auth_manager)

app = Flask(__name__, 
			template_folder='templates',
			static_folder='static')

from datetime import datetime, time

# get the current time object
def get_current_time():
  return datetime.now().time()

# create a time object (24 hour clock)
# for example, get_time(13,0,0) is 1:00 PM
def get_time(hours, minutes, seconds):
  return time(hours, minutes, seconds)

# compare the current time with 6:00 PM and 6:00 AM (inclusive)
# return True if we need to be using light mode
# return False if we should use dark mode
# use the functions above ^
def use_light_mode():
  if get_current_time() < get_time(6,0,0) and get_current_time() > get_time(18,0,0):
    return True
  return False

# returns a list of lists
# each list has an artist and their next concert, concert dates, and venue
def get_upcoming_concerts():
  return [
    ["Kendrick Lamar", "Rolling Loud - July 22-24 -Miami, FL"],
    ["The Weeknd", "Levi's Stadium - August 27 - Santa Clara, CA"],
    ["Russ", "Greek Theatre - May 1 - Berkeley, CA"]
  ]

'''
Get recommended songs
(at least one of seed_artists, seed_tracks and seed_genres are needed)
'''
def get_recommendations(seed_artists=None, seed_tracks=None, seed_genres=None):
  # check that at least one of the three parameters is not empty
  print("TODO: update this conditional")
  if True:
    # call the sp.recommendations function from the spotipy API
    print("TODO")
    # peek at the structure of the object returned by spotipy
    print("TODO")
    # return only the recommended song information
    print("TODO")

def get_playlists(spotify_user_id):
  # call the sp.user_playlists function, set limit to 10, store output in a variable
  print("TODO: Get results")
  results = None
  # from the result, keep only the songs (hint: print the result). call this new array tracks
  print("TODO: Create tracks")
  tracks = None
  # while there is a "next" value in the result
  while results and results["next"]:
    results = sp.next(results) 
    tracks.extend(results['items'])
  return tracks

@app.route('/')
@app.route('/playlists') # added another route 
def playlists():
  return render_template(
    "playlists.html", 
    use_light_mode=use_light_mode(),
    # TODO: pass info from get_playlists to your webpage
  )

@app.route('/recommendations') # recommendation 
def recommendations():
  return render_template(
    "recommendations.html", 
    use_light_mode=use_light_mode(), 
    concerts=get_upcoming_concerts(),
    # TODO: pass info from get_playlists to your webpage
  )

app.run(host='0.0.0.0', port=8080)
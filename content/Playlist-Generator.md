Title: Playlist Generator - a web application using Flask
Date: 2022-05-30
Category: Python
Summary: Building a web application using Flask
opengraph_image: newsaggregator.jpg


- This article is about my recent side project, building a web application using 
    - Flask(a micro web framework written in Python), 
    - PostgreSQL for database, 
    - HTML/CSS for frontend, 
    - Heroku for deployment

**Note: This project is just to demonstrate coding patterns and NOT for commercial purposes.**

#### What/Why this application?
- We usually like different playlists from different providers, e.g., I like "Weekly Top 20: English" from Wynk and also LastFM's "Top Tracks" playlist. But having these playlists in a single place(Spotify) is very convenient
- Using this application, users can select any listed playlist from available providers like LastFM, BillBoard, etc., and can directly create those playlists in their Spotify account with few clicks.

![playlists]({static}images/playlists.png)


##### This article documents how I went about building this feature in Flask:
- I have used [Spotify's Web API](https://developer.spotify.com/) to handle authorization. Spotify provides good documentation on authorization, different endpoints to access the User's data, and how to send requests to Spotify API on the user's behalf to create playlists and add items to playlists.

###### Authorization: 
 
```python 

base_url = 'https://accounts.spotify.com'

@app.route('/authorize')
def authorize():
    auth_url = f'{base_url}/authorize?client_id={client_id}&response_type=code&redirect_uri={redirect_uri}&scope={scope}'

    return redirect(auth_url)
```

- Here Scopes provide Spotify users using third-party apps the confidence that only the information they choose to share will be shared, and nothing more. When a user attempts to create a playlist, they will be redirected to log in to Spotify. Once they log in and provide authorization, then Spotify redirects to the callback URL, which should match the redirect URL in our Spotify developer account. 

```python
@app.route('/callback')
def callback():
    code = request.args.get('code')

    token_url = f"{base_url}/api/token"

    headers = {
        'Authorization': f"Basic {client_creds_b64.decode()}",
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    body = {
        'grant_type': 'authorization_code',
        'code': str(code),
        'redirect_uri': redirect_uri
    }

    response = requests.post(token_url, headers=headers, data=body)
    json_response = response.json()
    session['access_token'] = json_response['access_token']
    session['refresh_token'] = json_response['refresh_token']
    # ..
    # ..
    # ..

    return redirect(url_for('play_list', id=session['prev_url']))
```

- Once Spotify redirects the request to '/callback', we need to send a post request to '{base_url}/api/token' with an encoded version of (ID:secret) along with the code received, redirect_uri in the body of the request as shown above. A successful request which has a status code of 200, returns 'access token' and 'refresh token'. This access token is used to make API calls on behalf of the user. I have used the flask session object to store these values.

###### Create playlist and add songs:
- By now, we have all essentials to Create a playlist and add songs to it on behalf of the user. These two are separate POST requests. 

`base_endpoint = 'https://api.spotify.com'`

```python
# Creating a playlist

def create_playlist(user_id, access_token, name):
    endpoint = f"{base_endpoint}/v1/users/{user_id}/playlists"
    headers = {
        "Authorization": f"Bearer {access_token}",
        'Content-Type': 'application/json'
    }
    body = json.dumps({
        'name': name,
        'description': 'By Playlist Generator',
        'public': False
    })
    response = requests.post(endpoint, headers=headers, data=body)

    if response.status_code == 201:
        return response.json()
    elif response.status_code == 401:
        return None
```

```python
# Adding songs to the playlist created in the above step

def add_songs(playlist_id, access_token, uris):
    endpoint = f"{base_endpoint}/v1/playlists/{playlist_id}/tracks"
    headers = {
        "Authorization": f"Bearer {access_token}",
        'Content-Type': 'application/json'
    }
    body = json.dumps({
        'uris': uris
    })
    response = requests.post(endpoint, headers=headers, data=body)

    if response.status_code == 201:
        return response.json()
    elif response.status_code == 401:
        return None


```

###### Auto-Update Feature:

- This application also provides the user an option to auto-update the desired playlist every week. For this, the user needs to create an account with this application, so that we can save the refresh token, playlist_id in the database. To implement this feature, I have used The association object pattern which is a variant on many-to-many, this is useful when we need an extra column, in this case, user_playlist_id, beyond the foreign keys to the left and right tables.

```python
class Subscriptions(db.Model):
    __tablename__ = 'subscriptions'
    
    user_id = db.Column(db.Integer, db.ForeignKey(
        'users.id'), primary_key=True)
    playlist_id = db.Column(db.Integer, db.ForeignKey(
        'playlists.id'), primary_key=True)

    user_playlist_id = db.Column(
        db.String(60), index=False, unique=False, nullable=True)

    subscribed_user = db.relationship("User", back_populates='user_playlists')
    subscribed_playlist = db.relationship(
        "Playlist", back_populates='playlist_users')
```

###### Getting playlists from different providers:
- Till now I have discussed Spotify Authorization, and playlist creation, but how did I get all these playlist data from different providers like LastFM, billboard, etc., into my database? For this, I have used the 'Web Scraping' technique. This is used when you need a large amount of information from a website but it doesn't have any API to access that data. Most of this data is unstructured data in the HTML format, and we need to process it and save it in our database. For this, I have chosen the 'Beautiful Soup' Library in Python due to its simplicity.

Below is the sample code for web scraping: 

`pip install beautifulsoup4`

```python
import requests
from bs4 import BeautifulSoup

url = 'https://wynk.in/music/playlist/weekly-top-20-english/bb_1527140401220'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
results = soup.find_all('div', class_='ml-4 flex flex-col lg:my-auto')
songs_list = []

for i in results:
        track = i.find(
            'div', class_='text-base line-clamp-1 text-title').a.text
        artist = i.find(
            'div', class_='text-xs text-subtitle-hover line-clamp-1').text
        songs_list.append(dict({'song': track, 'artist': artist}))
```

*Remember that Web scraping is a kind of grey area, so check with the website's terms if you are using it for commercial purposes also web scraping consumes server resources for the host website. If we just scrape one page once, it would be ok, but if our code scrapes 1000s of pages, then it will get expensive for the website owner. So please avoid that.*


###### Deployment:
- I have chosen Heroku, a popular cloud hosting platform, which is very friendly for python applications. It has a free service tier that allows us to deploy our application without spending any money. 
- I have referenced [Miguel's Post](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xviii-deployment-on-heroku) for this deployment.
- For us to open this application for a broader user base we need to submit a quota extension request in the Spotify developer account. I prefer not to use that since this is a hobby project.
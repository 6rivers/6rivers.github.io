Title: News aggregator web app
Date: 2022-10-09
Category: Python
Summary: Building a News aggregator web app using Flask
opengraph_image: newsaggregator.jpg


This is about a web app, "News Aggregator" that serves users with daily News from different sources. It is built using Flask for the backend, and HTML / CSS for the frontend. This is a simple news aggregator that displays the Title, URL for the news with an image. It has different news categories like World, India, sports, etc. The final version of the web app can be seen at [News Aggregator](https://news-aggregator-i0e5.onrender.com/) and the complete code at my [GitHub Repo](https://github.com/6rivers/news-aggregator)

# Database:
The database for this application would have just two tables. One is to store the list of News sources(Source Table) and the other one is for news title, url, image_url, category, etc. These two tables have a relationship.

```python


class Source(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(24), nullable=False)
    image_url = db.Column(db.Text)
    news = db.relationship('News', backref='news_source', lazy='dynamic')


class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    url = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.Text, nullable=False)
    pub_date = db.Column(db.String(64), nullable=False)
    category = db.Column(db.String(12), nullable=False)
    source_id = db.Column(db.Integer, db.ForeignKey('source.id'))


```

# News Source:
To source the news, I have used RSS feeds from different news outlets and also NewsAPI.  "requests" and "BeautifulSoup" libraries were used for the web scraping process.

# News from RSS feeds:

```python
import requests
from bs4 import BeautifulSoup
from application import db
from application.models import News, Source

url = "https://www.yahoo.com/news/rss"
source = 'Yahoo News'
category = 'world'
headers = {'User-Agent': 'Mozilla/5.0'}

try:
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()  # Raise an error for bad status codes
    soup = BeautifulSoup(response.content, 'lxml-xml')
    items = soup.find_all('item')

    if not items:
        print(f"No items found in RSS feed for {source}")

    for item in items:
        try:
            # Safely extract data with fallbacks
            title = item.title.text if item.title else "No Title"
            link = item.link.text if item.link else ""

            # Handle optional image element
            img = item.find('media:content')
            img_url = img['url'] if img and img.has_attr('url') else ""

            pub_date = item.pubDate.text if item.pubDate else ""

            # Skip if essential fields are missing
            if not link:
                continue

            s = Source.query.filter_by(name=source).first()
            news = News(title=title, url=link, image_url=img_url,
                        pub_date=pub_date, category=category, news_source=s)
            db.session.add(news)

        except AttributeError as e:
            print(f"Error parsing item: {e}")
            continue

    db.session.commit()

except requests.exceptions.RequestException as e:
    print(f"Error fetching RSS feed: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
    db.session.rollback()
```

**Note on Error Handling:** The updated code above includes error handling to make the scraper more robust:
- Handles network failures and timeouts
- Checks for missing HTML elements before accessing them
- Validates that essential fields exist before creating database records
- Uses database rollback on errors to maintain data integrity

This is crucial for web scraping since website structures can change unexpectedly.

# News from NewsAPI

Another way to get news data is from [NewsAPI](https://newsapi.org/), through its JSON API. It provides an APIKey if we register(free) with them, to send API requests

```python
import requests
from application.models import News, Source

url = "https://newsapi.org/v2/top-headlines"
apiKey = "API Key you've got from NewsAPI"
params = {
    'country': 'in',
    'category': 'sports',
    'q': 'cricbuzz',
    'sortBy': 'top',
    'apiKey': apiKey
}
response = requests.get(url, params=params)
response = response.json()
articles = response['articles']
# find the complete code at my GitHub repo
```

After we get the data, we can save the required fields to the database tables as shown above.

# App Routing:

```python
from flask import render_template
from application import app
from application.models import News


@app.route('/')
def index():
    category = 'india'
    news = News.query.filter_by(category=category).all()
    return render_template('index.html', news=news)


```

# Deployment:

To deploy this web app I have used [Render](https://render.com/docs/deploy-flask), you can find the final version of this web app at [News Aggregator](https://news-aggregator-i0e5.onrender.com/)

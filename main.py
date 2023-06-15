import requests
from send_email import send_email


topics = ["q=tesla", "q=apple", "country=us&category=business",
          "sources=techcrunch", "domains=wsj.com"]

# Get your API key from https://newsapi.org/
api_key = "25598cc03b8b4ed9ba7dd3a169fa124c"

message = """\
Subject: Today's News

"""
for topic in topics:
    if topic == "country=us&category=business":
        url = "https://newsapi.org/v2/top-headlines?" \
              "country=us&category=business&" \
              "sortBy=popularity&" \
              "pageSize=20&" \
              "language=en&" \
              "apiKey=25598cc03b8b4ed9ba7dd3a169fa124c"
    else:
        url = "https://newsapi.org/v2/everything?" \
              f"{topic}&" \
              "sortBy=popularity&" \
              "pageSize=20&" \
              "language=en&" \
              "apiKey=25598cc03b8b4ed9ba7dd3a169fa124c"

    # Make request
    request = requests.get(url)

    # Get a dictionary with data
    content = request.json()

    # Access the article titles and description
    for article in content["articles"]:
        if article["title"] is not None:
            title = article["title"]
            description = article["description"]
            link = article["url"]
            message = message + f"""
    {title}
    {description}
    {link}
    \n
    """

message = message.encode('utf-8')
send_email(message)

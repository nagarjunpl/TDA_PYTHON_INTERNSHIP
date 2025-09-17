import requests   # to fetch data from the internet

API_KEY = "YOUR_REAL_NEWSAPI_KEY"

# Here we ask for top news headlines from India
url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=" + API_KEY
response = requests.get(url)   # connect to the API website

print("Status Code:", response.status_code)   # 200 means OK

data = response.json()
if data["status"] == "ok":
    print("\n✅ Latest News Headlines:\n")
    articles = data["articles"]

    # Loop through the news list
    for number, article in enumerate(articles, start=1):
        print(f"{number}. {article['title']}")     # show headline
        print(f"   Source: {article['source']['name']}")  # show news source
        print(f"   Link: {article['url']}\n")     # show link
else:
    print("❌ Failed to fetch news. Please check your API key.")

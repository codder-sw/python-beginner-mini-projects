import requests

# Asking user what topic they want news about
query = input("Enter topic you want news on (e.g. AI, cricket, politics, cloud, research): ")

api = "c7aff1ac559d45268e0e19bb83ecfa7e"

# API URL without country filter — global news
url = f"https://newsapi.org/v2/everything?q={query}&sortBy=publishedAt&apiKey={api}"

print(f"\nFetching latest news about '{query}'...\n")

r = requests.get(url)
data = r.json()

# Check API status
if data.get("status") != "ok":
    print("❌ Error fetching news:", data.get("message"))
else:
    articles = data.get("articles", [])

    if not articles:
        print("⚠️ No articles found for this topic. Try another keyword.")
    else:
        for article in articles[:10]:  # Show only first 10 articles
            print("📰", article.get("title"))
            print("📄", article.get("description"))
            print("🔗", article.get("url"))
            print("-" * 60)

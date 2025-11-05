# Importing the requests library to make API (internet) calls
# "requests" lets Python talk to websites and fetch data
import requests

# Asking the user to type a topic/category they want news about
# input() function takes user input from keyboard
query = input("Enter topic you want news on (e.g. AI, cricket, politics, cloud, research): ")

# This is your unique API key from NewsAPI website
# It is like a password to access the news server
api = "c7aff1ac559d45268e0e19bb83ecfa7e"

# Creating the URL (address) to request news data from the API
# f-string is used to insert Python variables inside the text
# q = topic we want, sortBy = show latest news first, apiKey = our API key to access data
url = f"https://newsapi.org/v2/everything?q={query}&sortBy=publishedAt&apiKey={api}"

# Printing message for user to show what news we are fetching
print(f"\nFetching latest news about '{query}'...\n")

# Sending request to the server and storing the response in 'r'
# requests.get(url) sends a GET request to NewsAPI to receive news data
r = requests.get(url)

# Converting the response into JSON format (dictionary-like format in Python)
# JSON = format in which API sends the data
data = r.json()

# Checking if the API responded successfully
# If status is not "ok", that means something went wrong
if data.get("status") != "ok":
    print("❌ Error fetching news:", data.get("message"))
else:
    # Extracting the list of news articles from the response
    # .get() avoids error if key doesn't exist
    articles = data.get("articles", [])

    # If no news articles are found for that topic
    if not articles:
        print("⚠️ No articles found for this topic. Try another keyword.")
    else:
        # Looping through first 10 news articles
        # [:10] means pick only first 10 results
        for article in articles[:10]:
            
            # Printing the title of the news article
            print("📰", article.get("title"))
            
            # Printing the short description of the news article
            print("📄", article.get("description"))
            
            # Printing the link to read full news article
            print("🔗", article.get("url"))
            
            # Printing a separator line to keep output clean
            print("-" * 60)

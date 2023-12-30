# Import feedparser, csv and requests modules
import feedparser
import csv
import requests

# Define the URL of the RSS feed
url = "http://www.hindustantimes.com/rss/topnews/rssfeed.xml"

# Parse the RSS feed using feedparser
d = feedparser.parse(url)

# Check if the feed is valid
if d.bozo == 0:
    # Save the RSS feed as an XML file
    with open("rssfeed.xml", "w", encoding="utf-8") as f:
        f.write(d.content.decode("utf-8"))

    # Create a list of dictionaries to store the news items
    news_list = []

    # Loop through the entries in the feed
    for entry in d.entries:
        # Create a dictionary to store the news item
        news_dict = {}
        # Store the title, link, summary and published date of the news item
        news_dict["title"] = entry.title
        news_dict["link"] = entry.link
        news_dict["summary"] = entry.summary
        news_dict["published"] = entry.published

        # Get the image URL from the summary using requests
        response = requests.get(entry.link)
        if response.status_code == 200:
            html = response.text
            start_index = html.find('<meta property="og:image" content="')
            if start_index != -1:
                end_index = html.find('"', start_index + 35)
                if end_index != -1:
                    image_url = html[start_index + 35:end_index]
                    news_dict["image_url"] = image_url

        # Append the dictionary to the list
        news_list.append(news_dict)

    # Save the news items as a CSV file
    with open("news.csv", "w", newline="", encoding="utf-8") as f:
        # Create a csv writer object
        writer = csv.writer(f)
        # Write the header row
        writer.writerow(["title", "link", "summary", "published", "image_url"])
        # Write the news items
        for news in news_list:
            writer.writerow([news["title"], news["link"], news["summary"], news["published"], news.get("image_url", "")])

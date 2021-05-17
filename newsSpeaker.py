import requests
import json

# importing the pyttsx library
import pyttsx3

# initialisation
engine = pyttsx3.init()

# testing


if __name__ == "__main__":
    # print("hello world")

    engine.say("Today's top Breaking News...")
    newsUrl = requests.get(
        "https://newsapi.org/v2/everything?q=Apple&from=2021-05-05&sortBy=popularity&apiKey=7a1a889cf05d4e4dbeb1e098dc00f6bd").text
    newsInJson = json.loads(newsUrl)
    mainArticle = newsInJson["articles"]

    for article in mainArticle:
        engine.say(article["title"])
        print(article["title"])
        with open("todayNews.txt", "a") as f:
            f.write(article["title"])
            f.write("\n")

    engine.runAndWait()
    print("That's all for today...")

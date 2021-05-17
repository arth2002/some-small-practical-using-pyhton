import pyshorteners


def shortner(link):
    short = pyshorteners.Shortener().tinyurl.short(link)
    # short_link = short.tinyurl.short(link)
    return short


url = input("Enter url here: ")
final = shortner(url)
print(f"shorted url: {final}")

import requests
from bs4 import BeautifulSoup

def get_html(url: str) -> str|None:
    try:
        result = requests.get(url)
        result.raise_for_status()
        return result.text
    except(requests.RequestException, ValueError):
        return None


def get_python_news() -> list|None:
    html = get_html("https://www.python.org/blogs/")
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        all_news = soup.find("ul", class_='list-recent-posts').findAll('li')
        result_news = []
        for news in all_news:
            title = news.find("a").text
            url = news.find("a")["href"]
            published = news.find("time").text
            result_news.append({
                "title": title,
                "url": url,
                "published": published,
            })
            print (result_news)
        return result_news
    return None

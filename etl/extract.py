import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

from url.url import URL

def extract():
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    raw_data = []

    for i in range(8):
        current_date = (
            datetime.today() - timedelta(days=i)
        ).strftime("%Y-%m-%d")

        page_url = f"{URL}?date={current_date}"

        response = requests.get(
            page_url,
            headers=headers
        )

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        articles = soup.find_all("article")

        for article in articles:
            title = article.find("h3")
            link = article.find("a")

            if title and link:
                raw_data.append({
                    "title": title.text.strip(),
                    "url": link.get("href"),
                    "publish_date": current_date
                })

    return raw_data
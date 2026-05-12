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

                news_url = link.get("href")

                detail_response = requests.get(
                    news_url,
                    headers=headers
                )

                detail_soup = BeautifulSoup(
                    detail_response.text,
                    "html.parser"
                )

                date_tag = detail_soup.find(
                    "div",
                    class_="detail__date"
                )

                publish_date = ""

                if date_tag:
                    publish_date = date_tag.text.strip()

                raw_data.append({
                    "title": title.text.strip(),
                    "url": news_url,
                    "publish_date": publish_date
                })

    return raw_data

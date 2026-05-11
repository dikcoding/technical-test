def transform(raw_data):

    cleaned_data = []

    for data in raw_data:
        title = data["title"].strip()
        url = data["url"].strip()

        publish_date = data["publish_date"]

        if title != "":

            cleaned_data.append({
                "title": title,
                "url": url,
                "publish_date": publish_date
            })

    return cleaned_data
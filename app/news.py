import requests


class NewsFeed:
    """Representing multiple news titles and links as a single string"""

    base_url = "http://newsapi.org/v2/everything?"
    api_key = "INSERT YOUR API KEY HERE"

    def __init__(
        self, interest: str, from_date: str, to_date: str, language: str = "en"
    ) -> None:
        self.interest = interest
        self.from_date = from_date
        self.to_date = to_date
        self.language = language

    def get(self) -> str:
        url = self._build_url()

        articles = self._get_articles(url)

        email_body = ""
        for article in articles:
            email_body = email_body + article["title"] + "\n" + article["url"] + "\n\n"

        return email_body

    def _get_articles(self, url: str) -> dict:
        response = requests.get(url)
        content = response.json()
        articles = content["articles"]
        return articles

    def _build_url(self) -> str:
        url = (
            f"{self.base_url}"
            f"qInTitle={self.interest}&"
            f"from={self.from_date}&"
            f"to={self.to_date}&"
            f"language={self.language}&"
            f"apiKey={self.api_key}"
        )
        return url


if __name__ == "__main__":
    news_feed = NewsFeed(
        interest="tech",
        from_date="2021-09-18",
        to_date="2021-09-19",
        language="en",
    )
    print(news_feed.get())

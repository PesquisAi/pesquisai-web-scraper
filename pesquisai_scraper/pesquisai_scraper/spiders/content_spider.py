from pathlib import Path

import scrapy


class QuotesSpider(scrapy.Spider):
    name = "content"

    def start_requests(self):
        urls = [
            "https://python-poetry.org/docs/cli/",
            "https://docs.scrapy.org/en/latest/intro/tutorial.html",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f"content-{page}.html"
        Path(filename).write_bytes(response.body)
        self.log(f"Saved file {filename}")

from scrapy.spiders import CrawlSpider
from scrapy.spiders import Rule
# from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst
import scrapy

from scraper.scraper.items import ScraperItem


class QuoteSpider(CrawlSpider):
    name = "properties"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = [
        "http://quotes.toscrape.com/"
    ]

    # def parse(self, response):
    #     for quote in response.css("div.quote"):
    #         yield {
    #             'text': quote.css("span.text::text").extract_first(),
    #             'author': quote.css("small.author::text").extract_first(),
    #             'tags': quote.css("div.tags > a.tag::text").extract()
    #         }

    #     next_page_url = response.css("li.next > a::attr(href)").extract_first()
    #     if next_page_url is not None:
    #         yield scrapy.Request(response.urljoin(next_page_url))

    rules = (
        Rule(
            # LinkExtractor(allow=("HouseDetails\.aspx")),
            callback="parse_quote",
            follow=True,
        ),
    )



    def parse_quote(self, response):
        quote_loader = ItemLoader(item=ScraperItem(), response=response)
        # quote_loader.default_output_processor = TakeFirst()

        quote_loader.add_css(
            "text", "span.text::text"
        )
        quote_loader.add_css(
            "author", "small.author::text"
        )

        yield quote_loader.load_item()
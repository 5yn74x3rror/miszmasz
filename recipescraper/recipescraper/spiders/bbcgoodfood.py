import scrapy


class BbcgoodfoodSpider(scrapy.Spider):
    name = "bbcgoodfood"
    allowed_domains = ["bbcgoodfood.com"]
    start_urls = ["https://www.bbcgoodfood.com/recipes/collection/quick-and-easy-family-recipes"]

    def parse(self, response):
        recipes = response.css('div.post__content article')

        for recipe in recipes:
            yield {
                'title': recipe.css('h2.heading-4::text').get(),
                'ratings_count': recipe.css('span.rating__count-text::text').get().replace(' ratings', ''),
                'description': recipe.css('div.card__description p').get().replace('<p>', '').replace('</p>', ''),
                'prep_time': recipe.css('ul.terms-icons-list li span').get(0).replace('<span class="terms-icons-list__text d-flex align-items-center" style="height:22px">', '').replace(' mins</span>', ''),
                'difficulty': recipe.css('ul.terms-icons-list li:nth-child(2) span').get(1).replace('<span class="terms-icons-list__text d-flex align-items-center" style="height:22px">', '').replace('</span>', ''),
                'url': recipe.css('div.card__content a').attrib['href'],
            }

        next_page = response.css('a.load-more-paginator__btn[data-component-variant="list-page-next"]').get()
        # print(next_page)
        if (next_page is not None):
            next_page_url = 'https://www.bbcgoodfood.com/recipes/collection/quick-and-easy-family-recipes?page=2'
            request = scrapy.Request(url=next_page_url)
            yield request
            # yield response.follow(next_page_url, callback=self.parse),

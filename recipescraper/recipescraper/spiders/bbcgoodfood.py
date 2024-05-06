import scrapy

from recipescraper.items import RecipeItem
from recipescraper.itemloaders import RecipeLoader

class BbcgoodfoodSpider(scrapy.Spider):
    name = "bbcgoodfood"
    allowed_domains = ["bbcgoodfood.com"]
    start_urls = ["https://www.bbcgoodfood.com/recipes/collection/quick-and-easy-family-recipes"]
    counter = 1

    def parse(self, response):
        recipes = response.css('div.post__content article')

        for recipe in recipes:
            recipe = RecipeLoader(item=RecipeItem(), selector=recipe)

            recipe.add_css('title', 'h2.heading-4::text')
            recipe.add_css('prep_time', 'ul.terms-icons-list li:nth-child(1) span', re='<span class="terms-icons-list__text d-flex align-items-center" style="height:22px">(.*)</span>')
            recipe.add_css('difficulty', 'ul.terms-icons-list li:nth-child(2) span', re='<span class="terms-icons-list__text d-flex align-items-center" style="height:22px">(.*)</span>')
            recipe.add_css('extra1', 'ul.terms-icons-list li:nth-child(3) span', re='<span class="terms-icons-list__text d-flex align-items-center" style="height:22px">(.*)</span>')
            recipe.add_css('extra2', 'ul.terms-icons-list li:nth-child(4) span', re='<span class="terms-icons-list__text d-flex align-items-center" style="height:22px">(.*)</span>')
            recipe.add_css('extra3', 'ul.terms-icons-list li:nth-child(5) span', re='<span class="terms-icons-list__text d-flex align-items-center" style="height:22px">(.*)</span>')
            recipe.add_css('ratings_count', 'span.rating__count-text::text')
            recipe.add_css('description', 'div.card__description p', re='<p>(.*)</p>')
            recipe.add_css('url', 'div.card__content a::attr(href)')
            
            yield recipe.load_item()

        next_page = response.css('a.load-more-paginator__btn[data-component-variant="list-page-next"]').get()

        if (next_page is not None):
            self.counter = self.counter + 1
            next_page_url = 'https://www.bbcgoodfood.com/recipes/collection/quick-and-easy-family-recipes?page=' + str(self.counter)
            yield scrapy.Request(url=next_page_url, callback=self.parse)

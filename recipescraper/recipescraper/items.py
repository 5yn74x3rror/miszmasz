# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class RecipeItem(scrapy.Item):
    title = scrapy.Field()
    ratings_count = scrapy.Field()
    description = scrapy.Field()
    prep_time = scrapy.Field()
    difficulty = scrapy.Field()
    url = scrapy.Field()
    extra1 = scrapy.Field()
    extra2 = scrapy.Field()
    extra3 = scrapy.Field()

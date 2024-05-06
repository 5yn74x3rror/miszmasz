from scrapy.loader import ItemLoader
from itemloaders.processors import MapCompose, TakeFirst

class RecipeLoader(ItemLoader):
    default_output_processor = TakeFirst()
    ratings_count_in = MapCompose(lambda x : x.split(' ')[0])
    prep_time_in = MapCompose(lambda x : x.split(' ')[0])
    url_in = MapCompose(lambda x : 'https://www.bbcgoodfood.com/recipes' + x)
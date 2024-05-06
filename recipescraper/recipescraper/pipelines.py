# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem

class RecipescraperPipeline:
    def process_item(self, item, spider):
        return item
    

class ExampleLbToKg:
    lb_to_kg_ratio = 2.2

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        if adapter.get('weight'):
            float_weight = float(adapter['weight'])
            adapter['weight'] = float_weight / self.lb_to_kg_ratio
            return item
        else:
            raise DropItem(f"Missing weight in {item}")


class DuplicatesPipeline:

    def __init__(self):
        self.recipes_seen = set()

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        if adapter['title'] in self.recipes_seen:
            raise DropItem(f"Duplicate recipe found: {item!r}")
        else:
            self.recipes_seen.add(adapter['title'])
            return item
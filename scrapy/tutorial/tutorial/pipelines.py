# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem


class TutorialPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        condition = True
        if condition:
            #adapter["foo"] = bar(adapter)
            return item
        print("Dropping item...")
        raise DropItem("Condition unsatisfied: {item}")

import scrapy


class Item(scrapy.Item):
    repo_name = scrapy.Field()
    repo_watch = scrapy.Field()
    repo_star = scrapy.Field()
    repo_fork = scrapy.Field()
    repo_size = scrapy.Field()
    repo_language = scrapy.Field()

# coding=utf8
# -*- coding: utf-8 -*-
from scrapy.crawler import CrawlerProcess
from github.spiders.github_spider import GithubSpider

process = CrawlerProcess()
# 指定多个spider
process.crawl(GithubSpider)
process.start()
print('000000000')

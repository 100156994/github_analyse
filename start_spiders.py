#开始爬虫，抓取数据
# coding=utf8
# -*- coding: utf-8 -*-
from scrapy.crawler import CrawlerProcess
from github.spiders.github_spider import GithubSpider

def start():
    process = CrawlerProcess()
    # 指定多个spider
    process.crawl(GithubSpider)
    process.start()

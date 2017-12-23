#!/usr/bin/python  
# coding: UTF-8
import random
from scrapy.downloadermiddlewares.httpproxy import HttpProxyMiddleware


class ProxyMiddleware(HttpProxyMiddleware):
    def __init__(self, proxies):
        self.proxies = proxies

    @staticmethod
    def proxy_shadowsocks():
        """ 使用 shadowsocks 代理 """
        proxy = "http://127.0.0.1:1080"
        return proxy

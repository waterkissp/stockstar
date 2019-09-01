# -*- coding: utf-8 -*-
import scrapy
import json


class JsonTestSpider(scrapy.Spider):
    name = 'json_test'
    allowed_domains = ['ooka.herokuapp.com']
    start_urls = ['https://ooka.herokuapp.com/accounts/profile/']

    def parse(self, response):
        title = response.css("title::text").extract()
        res = json.loads(response.text)
        print(res["state"])
        print(res["code"])

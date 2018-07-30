# -*- coding: utf-8 -*-
import json
from scrapy import Spider
from scrapy.selector import Selector

from youtube.items import YoutubeItem


class TopicYoutubeSpider(Spider):
    name = "youtube"
    allowed_domains = ["gdata.youtube.com"]
    start_urls = ['http://gdata.youtube.com/feeds/api/standardfeeds/DE/most_popular?v=2&alt=json']

    def parse(self, response):
        jsonresponse = json.loads(response.body_as_unicode())
        for video in jsonresponse["feed"]["entry"]:
            item = YoutubeItem()
            print video["media$group"]["yt$videoid"]["$t"]
            print video["media$group"]["media$description"]["$t"]
            item ["title"] = video["title"]["$t"]
            print video["author"][0]["name"]["$t"]
            print video["category"][1]["term"]
            yield item

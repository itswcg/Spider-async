# -*- coding: utf-8 -*-
# @Author  : itswcg
# @File    : toutiao.py
# @Time    : 19-2-14 上午11:20
# @Blog    : https://blog.itswcg.com
# @github  : https://github.com/itswcg

from ruia import Request, Spider

from items import TouTiaoItem
from middlewares import middleware
from db import MotorBase
from ruia_pyppeteer import PyppeteerSpider as Spider
from ruia_pyppeteer import PyppeteerRequest as Request


class TouTiaoSpider(Spider):
    start_urls = ['https://www.toutiao.com']
    concurrency = 3
    load_js = True

    async def parse(self, response):
        # self.mongo_db = MotorBase().get_db('hacknews')
        urls = ['https://www.toutiao.com/a6657312181127741965/']
        for index, url in enumerate(urls):
            yield Request(
                url,
                callback=self.parse_item,
                load_js=self.load_js
            )

    async def parse_item(self, response):
        print(response.html)
        async for item in TouTiaoItem.get_items(html=response.html):
            yield item

    async def process_item(self, item):
        # try:
        #     await self.mongo_db.toutiao.update_one({
        #         'url': item.url},
        #         {'$set': {'url': item.url, 'title': item.title}},
        #         upsert=True)
        # except Exception as e:
        #     self.logger.exception(e)
        print(item)


if __name__ == '__main__':
    TouTiaoSpider.start(middleware=middleware)

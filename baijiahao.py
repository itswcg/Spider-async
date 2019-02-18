# -*- coding: utf-8 -*-
# @Author  : itswcg
# @File    : hack_news.py
# @Time    : 19-2-13 下午2:28
# @Blog    : https://blog.itswcg.com
# @github  : https://github.com/itswcg

from ruia import Request, Spider

from items import BaiJiaHaoItem
from middlewares import middleware
from db import MotorBase


class BaiJiaHaoSpider(Spider):
    start_urls = ['https://baijiahao.baidu.com']
    concurrency = 3

    async def parse(self, response):
        self.mongo_db = MotorBase().get_db('hacknews')
        urls = ['https://baijiahao.baidu.com/s?id=1553475025395018',
                'https://baijiahao.baidu.com/s?id=1570895803249513']
        for index, url in enumerate(urls):
            yield Request(
                url,
                callback=self.parse_item,
                metadata={'index': index}
            )

    async def parse_item(self, response):
        async for item in BaiJiaHaoItem.get_items(html=response.html):
            yield item

    async def process_item(self, item):
        # try:
        #     await self.mongo_db.baijiahao.update_one({
        #         'url': item.url},
        #         {'$set': {'url': item.url, 'title': item.title}},
        #         upsert=True)
        # except Exception as e:
        #     self.logger.exception(e)
        print(item)


if __name__ == '__main__':
    BaiJiaHaoSpider.start(middleware=middleware)

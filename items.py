# -*- coding: utf-8 -*-
# @Author  : itswcg
# @File    : items.py
# @Time    : 19-2-13 下午2:29
# @Blog    : https://blog.itswcg.com
# @github  : https://github.com/itswcg

from ruia import AttrField, TextField, Item


class BaiJiaHaoItem(Item):
    target_item = TextField(css_select='div.article')
    title = TextField(css_select='div.article-title')
    content = TextField(css_select='div.article-content')


class TouTiaoItem(Item):
    target_item = TextField(css_select='div.article-box')
    title = TextField(css_select='h1.article-title')
    content = TextField(css_select='div.article-content')

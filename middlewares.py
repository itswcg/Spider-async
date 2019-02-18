# -*- coding: utf-8 -*-
# @Author  : itswcg
# @File    : middleware.py
# @Time    : 19-2-13 下午2:29
# @Blog    : https://blog.itswcg.com
# @github  : https://github.com/itswcg

from ruia import Middleware

middleware = Middleware()


@middleware.request
async def handle(request):
    ua = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    request.headers.update({'User-Agent': ua})

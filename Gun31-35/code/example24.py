# Translated to Turkish by himmetcanumutlu

"""
aiohttp - asenkron HTTP ağ erişimi
Asenkron I/O (asenkron programlama) - kullanıcı isteklerini işlemek için yalnızca tek iş parçacığı kullanır
Kullanıcı isteği kabul edildikten sonra geri kalan her şey I/O işlemidir; çoklu I/O çoğullama ile eş zamanlılık sağlanabilir
Bu yaklaşım çok iş parçacığına kıyasla CPU kullanımını artırır, çünkü iş parçacığı geçiş maliyeti yoktur
Redis/Node.js - tek iş parçacığı + asenkron I/O
Celery - zaman alan görevleri asenkronlaştırır
Asenkron I/O olay döngüsü - uvloop
"""
import asyncio
import re

import aiohttp


async def fetch(session, url):
    async with session.get(url, ssl=False) as resp:
        return await resp.text()


async def main():
    pattern = re.compile(r'\<title\>(?P<title>.*)\<\/title\>')
    urls = ('https://www.python.org/',
            'https://git-scm.com/',
            'https://www.jd.com/',
            'https://www.taobao.com/',
            'https://www.douban.com/')
    async with aiohttp.ClientSession() as session:
        for url in urls:
            html = await fetch(session, url)
            print(pattern.search(html).group('title'))


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()

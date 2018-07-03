import re

from bs4 import BeautifulSoup
from requests_html import HTMLSession
from util import *


class EatCrawler():
    session = None
    category = "eat"
    file_name = 'data/eat_crawler.json'

    def __init__(self):
        if not os.path.exists("data"):
            os.makedirs("data")
        data = load_json(self.file_name)
        self.items = data.get('items', {})
        self.session = HTMLSession()
        self.eat_items = []
        self.parse()
        write_json(self.file_name, {'items': self.items})

    def parse(self):
        res = self.session.get("http://crystalpot.cn/menu")
        for link in res.html.find('h4'):
            if len(link.absolute_links) > 0:
                if 'http://crystalpot.cn/menus/0' in link.absolute_links:
                    break
                url = link.absolute_links.pop()
                date = re.findall(r"\d+\.?\d*", url).pop()
                data_name = 'data/' + date + '_eat.json'
                if not os.path.exists("data"):
                    os.makedirs("data")
                item = {'id': date}
                info = []
                session = HTMLSession()
                res = session.get(url)
                # print(res.html.find('.m-article'))
                content = res.html.find('.m-article', first=True).raw_html.decode("utf-8")
                soup = BeautifulSoup(content)
                for p in soup.find_all('p'):
                    info.append(p.text)
                    if '网易餐厅' in p.text:
                        info = []
                    if '咖啡吧西餐' in p.text:
                        item['NetEase'] = info
                        info = []
                    if '西可餐厅' in p.text:
                        if 'NetEase' not in item:
                            item['NetEase'] = info
                            info = []
                        item['CoffeeBar'] = info
                        info = []
                    if '东忠餐厅' in p.text:
                        item['XiKe'] = info
                        info = []
                    if '英飞特餐厅' in p.text:
                        item['DongZhong'] = info
                        info = []
                if 'DongZhong' not in item:
                    item['DongZhong'] = info
                    info = []
                item['Infeite'] = info
                if item['id'] not in self.items or data_changed(self.items[item['id']], item):
                    self.items[item['id']] = item
                    self.eat_items.append(item)
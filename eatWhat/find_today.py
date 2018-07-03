from bs4 import BeautifulSoup
from requests_html import HTMLSession
from util import *

session = HTMLSession()


def eat_get(date):
    url = 'http://crystalpot.cn/menus/' + date
    file_name = 'data/' + date + 'eatWhat'
    if not os.path.exists("data"):
        os.makedirs("data")
    data = load_json(file_name)
    item = {}
    info = []
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
    print(item['DongZhong'])
    # write_json(file_name, item)


if __name__ == '__main__':
    eat_get('70650')

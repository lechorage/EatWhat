import leancloud

from eat_crawler import *



def object_id_key(name, id_value):
    return name + "_" + str(id_value)


def leancloud_object(name, data, id_key='id'):
    DataObject = leancloud.Object.extend(name)


def update_data():
    eat = EatCrawler()


if __name__ == '__main__':
    update_data()

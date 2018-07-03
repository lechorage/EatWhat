import json
import os



DEFAULT_IMAGE_URL = 'https://i.imgur.com/slYAXU0.jpg'


def load_json(file_name, default=dict):
    if os.path.exists(file_name):
        with open(file_name) as json_data:
            d = json.load(json_data)
            return d
    else:
        return default()


def write_json(file_name, json_data):
    print('writing:' + file_name)
    with open(file_name, 'w') as outfile:
        json.dump(json_data, outfile, ensure_ascii=False)
        print('writing done:' + file_name)
        return True


def ordered(obj):
    if isinstance(obj, dict):
        return sorted((k, ordered(v)) for k, v in obj.items() if k is not None and v is not None)
    if isinstance(obj, list):
        return sorted(ordered(x) for x in obj if x is not None)
    if obj is None:
        return ""
    else:
        return obj


def data_changed(local_item, item):
    return ordered(local_item) != ordered(item)


def upload_image(im, origin_url, name, default_url):
    try:
        print(origin_url)
        uploaded_image = im.upload_image(url=origin_url, title=name)
        return uploaded_image.link
    except Exception as e:
        print(e)
        return default_url


host = 'api.cognitive.microsofttranslator.com'
path = '/translate?api-version=3.0'

params = "&to=zh-Hans"



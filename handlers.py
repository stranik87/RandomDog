import requests
from settings import URL


def get_last_update():
    url = URL + 'getUpdates'
    r = requests.get(url)
    return r.json()['result'][-1]


def start(chat_id, first_name):
    url = URL + 'sendMessage'
    data = {
        'chat_id': chat_id,
        'text': "Assalomu alaykum {}. kuchukchani bosing!".format(first_name),
        'parse_mode': 'HTML',
        'reply_markup': {
            'keyboard': [['🐶']],
            'resize_keyboard': True
        }
    }
    requests.post(url, json=data)


def dog(chat_id):
    r = requests.get('https://random.dog/woof.json')
    img_url = r.json()['url']

    url = URL + 'sendPhoto'
    data = {
        'chat_id': chat_id,
        'photo': img_url
    }
    requests.post(url, json=data)
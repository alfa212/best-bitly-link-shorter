import os
import argparse

import requests
from urllib.parse import urlparse
from dotenv import load_dotenv
load_dotenv()


def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('url')

    return parser


def shorten_link(shorten_url, headers, input_link):
    payload = {"long_url": input_link}

    response = requests.post(shorten_url, json=payload, headers=headers)
    response.raise_for_status()

    return response.json()['link']


def count_clicks(url, headers):
    url = urlparse(url)
    clean_url = f'{url.netloc}{url.path}'
    response = requests.get(f'https://api-ssl.bitly.com/v4/bitlinks/{clean_url}/clicks/summary', headers=headers)
    response.raise_for_status()

    return response.json()['total_clicks']


def is_bitlink(url, headers):
    url = urlparse(url)
    clean_url = f'{url.netloc}{url.path}'
    response = requests.get(f'https://api-ssl.bitly.com/v4/bitlinks/{clean_url}', headers=headers)

    return response.ok


def main():
    shorten_url = 'https://api-ssl.bitly.com/v4/bitlinks'
    bitly_token = os.getenv('BITLY_TOKEN')
    # input_link = input('Введите ссылку:')
    input_link = createParser().parse_args().url
    headers = {
        'Authorization': f'Bearer {bitly_token}'
    }

    try:
        if is_bitlink(input_link, headers):
            print(f"Количество кликов {count_clicks(input_link, headers)}")
        else:
            print(f"Битлинк {shorten_link(shorten_url, headers, input_link)}")
    except requests.exceptions.HTTPError:
        print('Возникла ошибка - проверьте ссылку и попробуйте снова')


if __name__ == '__main__':
    main()

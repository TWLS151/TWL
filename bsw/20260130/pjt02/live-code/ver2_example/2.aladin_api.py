import requests
from pprint import pprint

# aladin api 를 활용하는 예시

url = 'http://www.aladin.co.kr/ttb/api/ItemSearch.aspx'


def get_data(api_key):
    params = {
        'ttbkey': api_key,
        'Query': '싸피',
        'QueryType': 'Title',
        'MaxResults': 10,
        'start': 1,
        'SearchTarget': 'Book',
        'output': 'js',
        'Version': 20131101,

    }
    response = requests.get(url, params=params).json()
    pprint(response)


if __name__ == '__main__':
    api_key = 'YOUR_API_KEY'
    get_data(api_key)


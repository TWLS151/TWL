import requests
from pprint import pprint

# dog api 를 활용하는 예시

url = 'https://dog.ceo/api/breeds/image/random'

def get_data():
    response = requests.get(url).json()
    print('response = ', response)


if __name__ == '__main__':
    get_data()


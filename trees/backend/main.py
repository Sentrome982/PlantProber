import requests

API_KEY = "Jr1pBQ9jaDulxwtmkjEzXhZwk86cgm1zrz7JeR8OZcU"
BASE_URL = 'https://trefle.io/api/v1/species?token='

def main(tree):
    tree = adjust(tree)
    request_url = f"{BASE_URL}{API_KEY}&filter[common_name]={tree}"
    response = requests.get(request_url)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return "An error occurred"


def adjust(tree):
    tree = tree.lower()
    split = tree.split()
    word=''
    for i in split:
        word+=i
        if i == split[-1]:
            pass
        else:
            word+='%20'
    return word


def sort(data):
    s_name = data['data'][0]['scientific_name']
    print(s_name)


print(sort(main("American beech")))
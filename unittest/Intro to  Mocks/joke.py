import requests


def len_joke():
    joke = get_joke()
    return len(joke)


def get_joke():
    url = 'https://v2.jokeapi.dev/joke/Any?safe-mode'
    response = requests.get(url)
    if response.status_code == 200:
        joke = response.json()['joke']
    else:
        joke = 'No jokes'

    return joke


if __name__ == '__main__':
    print(get_joke())

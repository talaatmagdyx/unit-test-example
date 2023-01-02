import requests


def len_joke():
    joke = get_joke()
    return len(joke)


def get_joke():
    url = 'https://v2.jokeapi.dev/joke/Any?safe-mode'
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
    except requests.exceptions.Timeout:
        return 'No jokes'
    except requests.exceptions.ConnectionError:
        pass
    except requests.exceptions.HTTPError as e:
        status_code = e.response.status_code
        return 'HTTPError was raise'

    else:
        if response.status_code == 200:
            joke = response.json()['joke']
        else:
            joke = 'No jokes'

        return joke


if __name__ == '__main__':
    print(get_joke())

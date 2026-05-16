import requests


def get_motivational_quote():
    url = "https://zenquotes.io/api/random"

    try:
        response = requests.get(url, timeout=5)

        if response.status_code == 200:
            data = response.json()

            quote = data[0]["q"]
            author = data[0]["a"]

            return f'"{quote}" — {author}'

        return "Não foi possível obter frase motivacional."

    except requests.RequestException:
        return "Erro ao conectar com a API."
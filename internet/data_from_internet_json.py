import requests
def main():
    url = 'http://javacream.eu:8080/people'
    responce = requests.get(url)
    data = responce.json()
    print(data)

main()
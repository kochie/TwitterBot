import requests


def main():
    session = requests.Session()
    session.auth = ("0cGBem05z7EyVhYXhobJhdedC", "O66Gkj4tgcAMyTUrIfXxY7fWiHU5nrAkOTCcqOr55YCPOdj9nt")
    root_url = "https://api.twitter.com/"
    response = session.post(url=root_url+"oauth2/token", data={"grant_type": "client_credentials"}, headers={"Content-Type": "application/x-www-form-urlencoded"})
    print(response.json())
    print(response.status_code)

    response = session.get(url=root_url+"1.1/statuses/user_timeline.json", headers={"Authorization": "Bearer {0}".format(response.json()['access_token'])})
    print(response.json())

if __name__ == '__main__':
    main()

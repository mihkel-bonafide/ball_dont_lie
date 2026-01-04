import requests
from hostfile import magic_key
BASE_URL = "https://api.balldontlie.io"


def request_player():
    print(f"hey bro.")
    player_search = input(f"Please type the name of the NBA player you wish to search: ")
    first, last = player_search.split(' ', 1)
    querystring = "https://api.balldontlie.io/v1/players?first_name=" + first + "&" + "last_name=" + last
    # print(querystring)  # confirm querystring format
    retrieve_id(querystring)

def retrieve_id(querystring):
    url = querystring
    payload = {}
    headers = {'Authorization': magic_key}

    response = requests.request("GET", url, headers=headers, data=payload).json()
    parsemeh = response["data"]
    dictmeh = parsemeh[0]
    player_id = dictmeh["id"]
    print(player_id)

# def retreive_player_season_stats(player_id):


def main():
    request_player()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass 
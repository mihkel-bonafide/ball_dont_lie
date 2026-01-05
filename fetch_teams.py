import json
from nba_api.stats.static import teams

"""
This script uses the nba.com API (?) to fetch basic team info (including a team id I suspect I'll 
need later)
"""

def get_teams():
    # module below fetches a list of 30 Python dictionary objects, each an NBA team
    nba_teams = teams.get_teams()
    print("Number of teams fetched: {}".format(len(nba_teams)))
    with open('teams_list.json', 'w') as output_file:
        json.dump(nba_teams, output_file, indent=2)


def main():
    get_teams()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass 
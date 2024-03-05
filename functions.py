import statsapi
import json
import numpy as np
from pathlib import Path

def generate_multiple_standings_json(year_range = []):
    """
    Takes in a list of two int values and generates all team standings between the two years
    """
    year_list = list(range(year_range[0], year_range[1] + 1))
    all_records = []
    
    for year in year_list:    
        params = {'leagueId':'103,104', 'season':year}
        standings = statsapi.get('standings', params)
        

        for divisions in standings['records']:
            all_records = all_records + divisions['teamRecords']

    base = Path('Data')
    json_path = base / (str(year_range[0]) + str(year_range[1]) + '.json')

    with open(json_path, "w") as file:
        json.dump(all_records, file, indent = 2)

def get_team_pct(team_id):
    """
    Takes in unique teamID and outputs list of the winning percentages (pct) for defined years
    TODO: Allow user to select which year range to take in - currently only static 2021-2023 for testing
    """

    with open('Data/20212023.json', 'r') as json_input:
        standings = json.load(json_input)

    team_pct = list(filter(lambda team: team['team']['id'] == team_id, standings))

    return team_pct
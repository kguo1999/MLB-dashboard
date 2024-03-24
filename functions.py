import statsapi
import json
import numpy as np
import pandas as pd
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
    Takes in unique teamID and outputs dataframe of the winning percentages (pct) for defined years
    TODO: Allow user to select which year range to take in - currently only static 2021-2023 for testing
    """

    # read json file
    with open('Data/20212023.json', 'r') as json_input:
        standings = json.load(json_input)

    # filter for specific team 
    team = list(filter(lambda team: team['team']['id'] == team_id, standings))
    
    # obtain year and winning pct as dataframe
    team_pct = [{'year': x['season'], 'pct': x['leagueRecord']['pct']} for x in team]
    team_pct = pd.DataFrame(team_pct)
    
    return pd.DataFrame(team_pct)

def get_season_standings(seasonNum = None):
    """
    Takes the season as input and gets the final MLB standings for all teams
    If season input is left blank, assumes CURRENT season with CURRENT standings if not yet complete
    """

    # get standings raw data
    standings_raw = statsapi.standings_data(leagueId = '103, 104', division = "all", season = seasonNum)

    # convert raw data into dataframe
    div_standings = [standings_raw[x] for x in standings_raw.keys()]
    standings = [team for item in div_standings for team in item['teams']]
    standings = pd.DataFrame(standings)

    # filter for columns we're interested in and sort by wins
    standings = standings[['name', 'w', 'l']].rename(columns = {'name':'Team Name', 'w': 'Wins', 'l': 'Losses'})
    standings['Win pct'] = standings['Wins'] / (standings['Wins'] + standings['Losses'])
    standings = standings.sort_values(by = 'Wins', ascending = False)

    return standings

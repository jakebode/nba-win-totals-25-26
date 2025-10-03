# update rosters for 2025-26 season
# saves to data/rosters/rosters_25_26/
# requires nba_api package: pip install nba_api

import time
import random

from nba_api.stats.endpoints import CommonTeamRoster

TEAM_IDS = {
    "ATL": 1610612737,
    "BOS": 1610612738,
    "BKN": 1610612751,
    "CHA": 1610612766,
    "CHI": 1610612741,
    "CLE": 1610612739,
    "DAL": 1610612742,
    "DEN": 1610612743,
    "DET": 1610612765,
    "GSW": 1610612744,
    "HOU": 1610612745,
    "IND": 1610612754,
    "LAC": 1610612746,
    "LAL": 1610612747,
    "MEM": 1610612763,
    "MIA": 1610612748,
    "MIL": 1610612749,
    "MIN": 1610612750,
    "NOP": 1610612740,
    "NYK": 1610612752,
    "OKC": 1610612760,
    "ORL": 1610612753,
    "PHI": 1610612755,
    "PHX": 1610612756,
    "POR": 1610612757,
    "SAC": 1610612758,
    "SAS": 1610612759,
    "TOR": 1610612761,
    "UTA": 1610612762,
    "WAS": 1610612764
}


def main():
    start_time = time.time()
    
    for abbr, id in TEAM_IDS.items():
        roster = CommonTeamRoster(team_id=id, season='2025-26')
        roster_data = roster.get_data_frames()[0]
        
        time.sleep(random.uniform(1.5, 3.5))
        roster_data.to_csv('data/rosters/rosters_25_26/'+f'{abbr.lower()}_2025_26_roster.csv')
    
    time_elapsed = time.time() - start_time
    print(f"done. process took {time_elapsed:.4f}s")


if __name__ == "__main__":
    main()

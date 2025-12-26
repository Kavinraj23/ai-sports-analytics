"""
This script fetches NBA player game logs for specified players using the nba_api library.
It retrieves game log data for each player and saves the combined data into a CSV file.
Run this script from the parent directory using:
python -m scripts.fetch_player_gamelogs
"""
from nba_api.stats.endpoints import playergamelog
from nba_api.stats.static import players
import pandas as pd

def fetch_player_gamelogs(player_names, season='2023-24'):
    all_gamelogs = {}
    for name in player_names:
        player_dict = players.find_players_by_full_name(name)
        if not player_dict:
            print(f"Player {name} not found.")
            continue
        player_id = player_dict[0]['id']
        gamelog = playergamelog.PlayerGameLog(player_id=player_id, season=season)
        gamelog_df = gamelog.get_data_frames()[0]
        all_gamelogs[name] = gamelog_df
    return all_gamelogs

if __name__ == "__main__":
    player_names = ["LeBron James", "Stephen Curry", "Kevin Durant"]
    gamelogs = fetch_player_gamelogs(player_names)

    all_games = []

    for name, df in gamelogs.items():
        print(f"\nGamelogs for {name}:\n")
        print(df.head())
        all_games.append(df)
    
    final_df = pd.concat(all_games, ignore_index=True)
    final_df.to_csv("data/player_gamelogs.csv", index=False)
    print("Saved player data")

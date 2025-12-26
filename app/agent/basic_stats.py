import pandas as pd

def load_data(path="data/player_gamelogs.csv"):
    df = pd.read_csv(path, parse_dates=["GAME_DATE"])
    df.columns = df.columns.str.lower()
    return df

def compute_ts_percent(df):
    return df["pts"] / (2 * (df["fga"] + 0.44 * df["fta"]))

def compute_recent_vs_season(df, player_id, num_games):
    player_df = df[df["player_id"] == player_id].sort_values("game_date")
    gp = len(player_df)

    if gp < num_games:
        return None

    recent = player_df.tail(num_games)
    season = player_df

    recent_ts = compute_ts_percent(recent).mean()
    season_ts = compute_ts_percent(season).mean()

    return {
        "games_played": gp,
        "recent_ts%": round(recent_ts, 3),
        "season_ts%": round(season_ts, 3),
        "delta": round(recent_ts - season_ts, 3)
    }
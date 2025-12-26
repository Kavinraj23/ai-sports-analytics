# get fastapi running
from fastapi import FastAPI
from app.schemas.analyze import AnalyzeRequest
from app.agent.basic_stats import load_data, compute_recent_vs_season

app = FastAPI()

@app.get("/health")
async def health():
    return {"status": "healthy"}

@app.post("/analyze")
async def analyze(request: AnalyzeRequest):
    df = load_data()
    stats = compute_recent_vs_season(df, request.player_id, request.num_games)
    if stats is None:
        return {
            "player_id": request.player_id,
            "num_games": request.num_games,
            "message": "Insufficient data for reliable analysis",
        }

    return {
        "player_id": request.player_id,
        "num_games": request.num_games,
        "games_played": stats["games_played"],
        "recent_ts%": stats["recent_ts%"],
        "season_ts%": stats["season_ts%"],
        "delta": stats["delta"],
    }
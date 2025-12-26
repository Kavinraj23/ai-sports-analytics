from pydantic import BaseModel

class AnalyzeRequest(BaseModel):
    player_id: int
    num_games: int
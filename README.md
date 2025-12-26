Project: AI Sports Analytics Agent (NBA)

Goal:
Answer natural-language questions about NBA player performance
using structured statistical analysis and an agent-based pipeline.

MVP Questions:
1. Is Player X underperforming in the last N games?
2. Which metrics explain the change?
3. How does recent performance compare to season average?

Out of Scope:
- Multiple sports
- Team-level strategy
- Deep learning models
- Frontend UI

Edge Cases:
- Check if a player is a rookie and has played less than N games
    - Rookie = First NBA Season
    - Insufficient Data = < N games

Tech Stack (initial):
- Python
- FastAPI
- PostgreSQL
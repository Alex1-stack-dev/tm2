from fastapi import FastAPI
import uvicorn
from models.models import get_all_athletes
app = FastAPI()
@app.get("/results")
def results():
    athletes = get_all_athletes()
    return [{"name": a.name, "team": a.team} for a in athletes]
def run_server():
    uvicorn.run(app, host="0.0.0.0", port=8000)

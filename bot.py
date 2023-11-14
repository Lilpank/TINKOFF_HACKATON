from fastapi import FastAPI
import requests
import json
import time
from config import *
from pydantic import BaseModel

app = FastAPI()

class Field(BaseModel):
    game_field: str

class Figure(BaseModel):
    figure: str

def connect():
    while True:
        payload = {"bot_id": bot_id, "password": bot_password, "bot_url": bot_url}
        r = requests.post(f"{mediator_address}/sessions/{session_id}/registration", 
                          headers={"Content-Type": "application/json"}, 
                          data=json.dumps(payload))
        if r.status_code == 200:
            fig = json.loads(r.text)['figure']
            return fig
        time.sleep(10)

fig = connect()

@app.post("/bot/turn")
async def make_turn(field: Field):
    s = field.game_field
    s = s.replace('_', fig, 1)

    return s


from fastapi import FastAPI
import requests
import json
import time
from config import *
from pydantic import BaseModel
from tictac import TicTacToe
from algorithm import *

args = {
    'C': 1.41,
    'num_searches': 25
}

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

tictactoe = TicTacToe()
mcts = MCTS(tictactoe, args)
state = tictactoe.get_initial_state()

figures = 'xo'

fig_bot = connect()
fig_opponent = figures.replace(fig_bot, '')

players = {'x': 1, 'o': -1}
players_ = {1: 'x', -1: 'o'}
player_bot = players[fig_bot]
player_opponent = players[fig_opponent]

indexies = set()

def train(player, s):
    global state, indexies
    neutral_state = tictactoe.change_perspective(state, player)
    mcts_probs = mcts.search(neutral_state)
    index = np.argmax(mcts_probs)
    state = tictactoe.get_next_state(state, index, player)

    s = s[:index] + players_[player] + s[index+1:]
    return s

def transform(s):
    s = np.array(list(s))
    n = np.where(s == 'o', -1, s)
    n = np.where(n == '_', 0, n)
    n = np.where(n == 'x', 1, n)
    n = n.reshape(19,19).astype('int64')

    return n

@app.post("/bot/turn")
async def make_turn(field: Field):
    t = time.time()

    global state, indexies
    
    s = field.game_field
    
    if (len(set(s))) == 1:
        return train(player_bot, s)
    
    state = transform(s)

    q = train(player_bot, s)
    elapsed = time.time() - t
    print(elapsed)

    return q
import os

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

FRONTEND_BUILD = './frontend/build'

if not os.path.isdir(FRONTEND_BUILD):
    os.mkdir(FRONTEND_BUILD)

app = FastAPI()

@app.get('/hello')
def get_items():
    return { 'text': 'hello' }

app.mount('/', StaticFiles(directory=FRONTEND_BUILD, html=True), name='static')

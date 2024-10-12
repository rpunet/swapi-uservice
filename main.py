from fastapi import FastAPI
import requests

SWAPI_URL = "https://swapi.dev/api/people/"

app = FastAPI()
@app.get("/people")
def get_people():
    response = requests.get(SWAPI_URL)
    people = response.json()

    return people

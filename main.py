from fastapi import FastAPI, HTTPException
import requests
import logging

app = FastAPI()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.get("/people")
def get_people():
    url = "https://swapi.dev/api/people/"
    people = []

    try:
        while url:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            people.extend(data["results"])
            url = data["next"]

        logger.info("Data fetched and sorted")
        return sorted(people, key=lambda item: item["name"])
    except:
        logger.error(f"Error fetching data")
        raise HTTPException(status_code=500, detail="xxx")

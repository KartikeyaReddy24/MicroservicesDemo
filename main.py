from fastapi import FastAPI
import uvicorn
from mylib.logic import wiki as wiki_logic
from mylib.logic import search_wiki

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "This is Wikipedia API Microservice. You can search anything by calling Call /search or /wiki"}


@app.get("/search/{value}")
async def search(value: str):
    """Page to search in wikipedia"""

    result = search_wiki(value)
    return {"result": result}


@app.get("/wiki/{name}")
async def wiki(name: str):
    """Retrive wikipedia page"""

    result = wiki_logic(name)
    return {"result": result}


@app.get("/phrase/{name}")
async def phrase(name: str):
    """Retrive wikipedia page and return phrases"""

    result = wiki_logic(name)
    return {"result": result}


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")

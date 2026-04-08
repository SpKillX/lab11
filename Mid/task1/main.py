from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()

GO_SERVICE_URL = "http://localhost:8080/book"

@app.post("/remote-book")
async def remote_book(payload: dict):
    try:
        response = requests.post(GO_SERVICE_URL, json=payload)
        return response.json()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
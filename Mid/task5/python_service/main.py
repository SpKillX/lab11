import os
import requests
from fastapi import FastAPI

app = FastAPI()

GO_SERVICE_URL = os.getenv("GO_SERVICE_URL", "http://go-app:8080")

@app.get("/")
def read_root():
    return {"message": "I am Python Service"}

@app.get("/fetch-go")
def fetch_from_go():
    try:
        response = requests.get(f"{GO_SERVICE_URL}/data", timeout=2)
        return {
            "python_status": "received",
            "go_response": response.json()
        }
    except Exception as e:
        return {"error": f"Could not connect to Go: {str(e)}"}
#test
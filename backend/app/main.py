from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="FLOWCAST API")

app.include_router(router)


@app.get("/")
def home():
    return {"message": "FLOWCAST server is running"}
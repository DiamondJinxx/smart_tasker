from fastapi import FastAPI

from .api import api_router


app = FastAPI(
    title="SMART Tasker App",
    description="App for controling your goals accoording to the SMART principles"
)

app.include_router(api_router)

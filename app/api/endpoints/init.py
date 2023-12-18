from fastapi import APIRouter


router = APIRouter(prefix='/init')

@router.get("/")
async def init_message():
    return {"message": "Hi from init route!!"}

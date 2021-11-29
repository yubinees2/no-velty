from fastapi import APIRouter

router = APIRouter(
    prefix='/test',
    tags=['test'],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def test_api():
    return {"msg":"Hello API test"}

@router.get("/status")
async def status_check():
    try:
        a = 1/0
    except Exception as e:
        return {"Error": str(e)}
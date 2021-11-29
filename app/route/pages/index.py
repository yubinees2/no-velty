from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")

router = APIRouter(
    prefix='/index',
    tags=['index'],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def home(request: Request):
    return templates.TemplateResponse("general/home.html", {"request": request})


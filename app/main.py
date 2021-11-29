from fastapi import FastAPI

from app.common.config import settings

from app.route.apis import test, api, auth
from app.route.pages import index, login

app = FastAPI(title=settings.PROJECT_NAME,
              version=settings.PROJECT_VERSION)

app.include_router(test.router)
app.include_router(api.router)
app.include_router(auth.router)
app.include_router(index.router)
app.include_router(login.router)

@app.get("/")
async def root():
    return {"message": "Hello root!"}
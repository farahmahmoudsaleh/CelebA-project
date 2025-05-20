from fastapi import FastAPI
from controller.routes import router
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.include_router(router)
app.mount("/static", StaticFiles(directory="view/static"), name="static")
templates = Jinja2Templates(directory="view/templates")

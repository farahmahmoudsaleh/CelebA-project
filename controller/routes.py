from fastapi import APIRouter, UploadFile, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from utils.image_utils import load_image, create_transforms
from model.predictor import predict_on_image
from model.model_loader import load_model

router = APIRouter()
templates = Jinja2Templates(directory="view/templates")

device, model = load_model()
_, val_transform = create_transforms()

@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@router.post("/predict")
async def predict(file: UploadFile):
    image = load_image(file)
    image_tensor = val_transform(image)
    predictions = predict_on_image(model, image_tensor, device)
    return predictions

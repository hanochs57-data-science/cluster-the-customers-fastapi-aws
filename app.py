from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import joblib
from numpy import round

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

model = joblib.load("model.pkl")

options = [
    "High-Value Loyalists",
    "Budget Seekers",
    "Window Shoppers",
    "Churn Risks",
    "Tech Innovators",
    "Passive Consumers",
    "Brand Advocates",
    "Urban Professionals",
    "Suburban Families",
    "Digital Nomads",
    "Seasonal Buyers",
    "Impulse Shoppers",
    "Discounts-Only Hunters",
    "Recent Onboarders",
]

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "request": request,
            "prediction": None
        }
    )

@app.post("/predict", response_class=HTMLResponse)
def predict(
    request: Request,
    Age: float = Form(...),
    Gender: str = Form(...),
    AnnualIncome: float = Form(...),
    SpendingScore: float = Form(...)
):
    prediction = model.predict([[
        Age,
        Gender,
        AnnualIncome,
        SpendingScore
    ]])
    predict_probability = model.predict_proba([[
        Age,
        Gender,
        AnnualIncome,
        SpendingScore
    ]])
    predicted_class = int(prediction[0])
    predicted_option = options[predicted_class]
    probability = predict_probability[0]

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "request": request,
            "prediction": predicted_option,
            "probability": probability
        }
    )

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.services.text_analyzer import analyze_text

router = APIRouter()


class TextRequest(BaseModel):
    text: str


@router.post("/analyze")
def analyze(request: TextRequest):
    text = request.text.strip()

    if not text:
        raise HTTPException(status_code=400, detail="Text cannot be empty")

    result = analyze_text(text)

    return result
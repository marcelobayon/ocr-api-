from fastapi import FastAPI, File, UploadFile
from app.ocr import extract_text

app = FastAPI()

@app.post("/ocr")
async def perform_ocr(file: UploadFile = File(...)):
    contents = await file.read()
    text = extract_text(contents)
    return {"text": text}

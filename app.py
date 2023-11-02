from fastapi import FastAPI, UploadFile, Form, HTTPException
from shelfietext.process import process_text
import os

app = FastAPI()


@app.post("/ocr/")
async def ocr_service(image: UploadFile = Form(...), lang: list[str] = Form(...)):
    # Save the uploaded image temporarily or process it in-memory
    image_path = "path_to_temporary_storage"

    with open(image_path, "wb") as buffer:
        buffer.write(image.file.read())

    # Call the refactored process_text function
    try:
        ocr_result = process_text(image_path, lang)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"OCR Processing Error: {e}")

    # Delete the temporary image file after processing (optional)
    os.remove(image_path)

    return {"text": ocr_result}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)

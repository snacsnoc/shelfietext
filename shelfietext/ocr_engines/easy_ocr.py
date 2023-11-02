import easyocr
from PIL import Image, ImageOps, ImageEnhance
from io import BytesIO

import easyocr
import numpy as np

def job_easy_ocr(_options):
    image_data = _options.get("data")
    if image_data:
        # Convert BytesIO stream back to PIL Image
        img_pil = Image.open(BytesIO(image_data))
        # Convert PIL Image to numpy array
        img_np = np.array(img_pil)
    else:
        img_np = _options["path"]  # Using file path if data is not provided

    reader = easyocr.Reader(_options["lang"])
    text = reader.readtext(img_np, detail=0)
    text = "".join(text)
    print("[*] job_easy_ocr", text)
    return text

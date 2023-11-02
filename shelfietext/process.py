from PIL import Image, ImageOps, ImageEnhance
from concurrent.futures import ThreadPoolExecutor
from io import BytesIO

from .ocr_engines import (
    job_easy_ocr,
    job_tesseract,
    job_gocr,
    job_ocrad,
)


def wrapper(func, args, queue):
    queue.put(func(args))


# custom error
class NoTextDetectedError(Exception):
    pass


def preprocess_image(image_file):
    """Preprocess the image for better OCR results."""
    img = Image.open(image_file)

    # Resize the image (2x scale)
    width, height = img.size
    resized = img.resize((width * 2, height * 2))

    # Convert the image to grayscale
    grayscale = ImageOps.grayscale(resized)

    # Enhance the contrast of the image
    enhancer = ImageEnhance.Contrast(grayscale)
    enhanced = enhancer.enhance(9)  # Increase contrast

    # Rotate the image
    rotated = enhanced.rotate(90, expand=True)

    return rotated




def process_text(image_file, lang: list[str], tesseract: dict = {}):
    """Process and detect text from an image using multiple OCR engines"""

    # Preprocess the image
    preprocessed_img = preprocess_image(image_file)

    # Convert the preprocessed image to byte stream
    image_data = BytesIO()
    preprocessed_img.save(image_data, format="PNG")

    options = {
        "data": image_data.getvalue(),
        "lang": lang,
        "tesseract": tesseract,
    }

    with ThreadPoolExecutor(max_workers=2) as executor:
        easyocr_result = executor.submit(job_easy_ocr, options)
        tesseract_result = executor.submit(job_tesseract, options)

    # Combine the results from the OCR engines into a list
    combined_result = [easyocr_result.result(), tesseract_result.result()]

    return combined_result


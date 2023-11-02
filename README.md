# ShelfieText

A specialized OCR system for processing book spines, built upon the capabilities of both EasyOCR and Tesseract. This project is an independent fork and adaptation of [BetterOCR](https://github.com/junhoyeo/BetterOCR) by [Junho Yeo](https://github.com/junhoyeo).

## Features

* **OCR Combination**: Utilizes the power of both EasyOCR and Tesseract to extract text from images.
* **Specialized for Book Spines**: Optimized for the unique challenges posed by text on book spines.
* **FastAPI Backend**: Provides a robust and efficient backend server for processing OCR requests via a RESTful API.

## Getting Started
Install packages:
```commandline
pip install -r requirements.txt
```
Create a `tessdata` folder with the trained data file:
```commandline
wget https://github.com/tesseract-ocr/tessdata/raw/main/eng.traineddata -O ./tessdata/eng.traineddata
```

### Running the server
After setting up, you can start the FastAPI server by running:
```commandline
uvicorn main:app
```

## Testing
The examples/ directory contains sample images that you can use to test the system.

Using curl:
```commandline
curl -X 'POST' 'http://127.0.0.1:8000/ocr/' \
  -H 'accept: application/json' \
  -F 'image=@examples/sample.jpg' \
  -F 'lang=en'

```

License
This project is licensed under the MIT License. See the LICENSE file for more details.
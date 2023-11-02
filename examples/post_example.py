import requests

API_ENDPOINT = "http://0.0.0.0:8000/ocr/"

# Define the path to your image and the language(s) for OCR
image_path = "dyl3.png"
languages = ["en"]

files = {"image": open(image_path, "rb")}
data = {"lang": languages}

# Send the POST request
response = requests.post(API_ENDPOINT, files=files, data=data)

# Print the response
print(response.json())

import sys
from shelfietext.process import process_text


def main(image_path):
    # Define the languages and any tesseract-specific configurations you want to use
    lang = ["en"]
    tesseract_config = {
        "config": "--tessdata-dir ./tessdata"
    }  # Any specific configurations for Tesseract if needed

    # Run the process_text function
    result = process_text(image_path, lang, tesseract_config)

    # Print the OCR result
    print(result)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python example.py <path_to_image>")
        sys.exit(1)

    image_path = sys.argv[1]
    main(image_path)

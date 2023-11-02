# Thanks to Junho Yeo https://github.com/junhoyeo

import pytesseract

from .mapping import LANG_CODE_MAPPING


def convert_to_tesseract_lang_code(langs: list[str]) -> str:
    return "+".join(
        [
            LANG_CODE_MAPPING[lang]
            for lang in langs
            if lang in LANG_CODE_MAPPING and LANG_CODE_MAPPING[lang] is not None
        ]
    )


from PIL import Image
import io

def job_tesseract(_options):
    lang = convert_to_tesseract_lang_code(_options["lang"])

    # Check if "data" is provided in _options. If so, convert it to an image.
    if "data" in _options:
        image_data = _options.get("data")
        img_pil = Image.open(io.BytesIO(image_data))
        img_source = img_pil
    else:
        img_source = _options["path"]

    text = pytesseract.image_to_string(
        img_source,  # This will handle both direct image data and path.
        lang=lang,
        **_options["tesseract"]
        # pass rest of tesseract options here.
    )

    text = text.replace("\n", "\\n")
    print("[*] job_tesseract_ocr", text)
    return text

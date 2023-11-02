from .process import (
    process_text,
    NoTextDetectedError,
)
from .ocr_engines import job_easy_ocr, job_tesseract, job_gocr, job_ocrad

__all__ = [
    "process",
    "process_text",
    "NoTextDetectedError",
    "job_easy_ocr",
    "job_tesseract",
    "job_gocr",
    "job_ocrad",
]

__author__ = "snacsnoc"

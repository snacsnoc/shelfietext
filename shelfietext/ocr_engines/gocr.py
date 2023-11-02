from subprocess import Popen, PIPE
import cv2
from PIL import Image
import io
import numpy as np

def job_gocr(_options):
    # Check if "data" is provided in _options. If so, convert it to a matrix format using cv2.
    if "data" in _options:
        image_data = _options.get("data")
        img_pil = Image.open(io.BytesIO(image_data))
        mat = np.array(img_pil)
    else:
        mat = cv2.imread(_options["path"])

    # Convert to grayscale if not already
    if len(mat.shape) == 3 and mat.shape[2] == 3:
        mat = cv2.cvtColor(mat, cv2.COLOR_BGR2GRAY)

    p = Popen(["gocr", "-"], stdin=PIPE, stdout=PIPE)
    retval, buf = cv2.imencode(".pgm", mat)

    p.stdin.write(buf)
    p.stdin.close()
    p.wait()
    text = p.stdout.read().decode("utf-8").strip("\n")
    p.stdout.close()

    print("[*] job_gocr", text)
    return text

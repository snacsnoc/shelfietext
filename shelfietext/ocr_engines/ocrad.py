from subprocess import Popen, PIPE
import cv2
from PIL import Image
import io
import numpy as np

def job_ocrad(_options):
    # Check if "data" is provided in _options. If so, convert it to a matrix format using cv2.
    if "data" in _options:
        image_data = _options.get("data")
        img_pil = Image.open(io.BytesIO(image_data))
        mat = np.array(img_pil)
        # Check if the image is not grayscale (i.e., it has more than one channel)
        if len(mat.shape) == 3 and mat.shape[2] > 1:
            mat = cv2.cvtColor(mat, cv2.COLOR_RGB2GRAY)
    else:
        mat = cv2.imread(_options["path"], cv2.IMREAD_GRAYSCALE)

    p = Popen(["ocrad", "-"], stdin=PIPE, stdout=PIPE)
    retval, buf = cv2.imencode(".pgm", mat)

    p.stdin.write(buf)
    p.stdin.close()
    p.wait()
    text = p.stdout.read()
    p.stdout.close()

    print("[*] job_ocrad", text)
    return text.decode(_options.get("encoding", "utf-8")).strip("\n")

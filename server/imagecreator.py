from PIL import Image
import numpy as np

def create_image(pixels):
    array = np.array(pixels, dtype=np.float32)
    return array
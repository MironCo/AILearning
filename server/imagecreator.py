from PIL import Image
import numpy as np

def create_image(pixels):
    # Convert to numpy array and reshape to 28x28
    array = np.array(pixels, dtype=np.float32).reshape(28, 28)

    # Normalize to 0-1 range (MNIST expects this)
    if array.max() > 1.0:
        array = array / 255.0

    # MNIST has white digits on black background
    # If your drawing is black on white, uncomment the next line:
    # array = 1.0 - array

    return array
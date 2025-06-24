import numpy as np
import sys
from PIL import Image

import warnings
warnings.filterwarnings('ignore')

def preprocessing(img):
    preprocessed_img = Image.open(img)
    preprocessed_img = preprocessed_img.convert("L")
    preprocessed_img = preprocessed_img.resize((50,50), Image.ANTIALIAS)
    preprocessed_img = np.asarray(preprocessed_img)/255
    preprocessed_img = preprocessed_img.reshape(-1, 50, 50, 1)

    return preprocessed_img

if __name__ == "__main__":
    img = sys.argv[1]
    result = preprocessing(img)
    print("Processed image shape:", result.shape)


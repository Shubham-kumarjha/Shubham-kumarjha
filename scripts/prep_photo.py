import sys
import cv2
import numpy as np
from PIL import Image
from rembg import remove

def prepare_image(input_path, output_path):
    try:
        input_img = Image.open(input_path)
        output_img = remove(input_img)
        output_img.save("no_bg.png")

        img = cv2.imread("no_bg.png", cv2.IMREAD_UNCHANGED)
        if img.shape[2] == 4:
            alpha = img[:, :, 3]
            gray = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)
            gray = cv2.bitwise_and(gray, gray, mask=alpha)
        else:
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
        enhanced = clahe.apply(gray)
        cv2.imwrite(output_path, enhanced)
        print("Photo prepared successfully!")
    except Exception as e:
        print(f"Error prepping photo: {e}")

if __name__ == "__main__":
    inp = sys.argv[1] if len(sys.argv) > 1 else "photo.jpg"
    out = sys.argv[2] if len(sys.argv) > 2 else "prepared_photo.png"
    prepare_image(inp, out)

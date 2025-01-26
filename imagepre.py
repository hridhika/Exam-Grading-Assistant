from PIL import Image, ImageEnhance
import cv2
import numpy as np

def preprocess_image(image_path, output_path):
    try:
        # Load the image
        img = Image.open(image_path)
        print(f"Original image size: {img.size}")
        img_resized = img.resize((800, 800))  
        print("Image resized.")
        enhancer = ImageEnhance.Contrast(img_resized)
        img_enhanced = enhancer.enhance(1.5)  # Increase contrast by 1.5x

        enhancer = ImageEnhance.Brightness(img_enhanced)
        img_enhanced = enhancer.enhance(1.2)  # Increase brightness by 1.2x
        print("Image enhanced.")

        img_enhanced.save(output_path)
        print(f"Processed image saved at: {output_path}")

        img_cv = cv2.imread(output_path, cv2.IMREAD_GRAYSCALE)
        laplacian_var = cv2.Laplacian(img_cv, cv2.CV_64F).var()
        print(f"Image sharpness (Laplacian variance): {laplacian_var}")
        
        if laplacian_var < 100:
            print("Warning: Image might be blurry.")

    except Exception as e:
        print(f"Error during preprocessing: {e}")

# Example usage
preprocess_image("input_image.jpg", "processed_image.jpg")

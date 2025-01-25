from PIL import Image, ImageEnhance
import cv2

def preprocess_image(image_path, output_path):
    try:
        # Load the image
        img = Image.open(image_path)
        print(f"Original image size: {img.size}")

        # Resize the image
        img_resized = img.resize((800, 800))  # Resize to 800x800 pixels
        print("Image resized.")

        # Enhance the image (contrast and brightness)
        enhancer = ImageEnhance.Contrast(img_resized)
        img_enhanced = enhancer.enhance(1.5)  # Increase contrast by 1.5x

        enhancer = ImageEnhance.Brightness(img_enhanced)
        img_enhanced = enhancer.enhance(1.2)  # Increase brightness by 1.2x
        print("Image enhanced.")

        # Save the processed image
        img_enhanced.save(output_path)
        print(f"Processed image saved at: {output_path}")

        # Verify image quality (e.g., sharpness) using OpenCV
        img_cv = cv2.imread(output_path, cv2.IMREAD_GRAYSCALE)
        laplacian_var = cv2.Laplacian(img_cv, cv2.CV_64F).var()
        print(f"Image sharpness (Laplacian variance): {laplacian_var}")

        if laplacian_var < 100:
            print("Warning: Image might be blurry.")
        
        return output_path  # Return processed image path
    except Exception as e:
        print(f"Error during preprocessing: {e}")
        return None

# Example usage
if __name__ == "__main__":
    input_image = "input_image.jpg"
    output_image = "processed_image.jpg"
    preprocess_image(input_image, output_image)
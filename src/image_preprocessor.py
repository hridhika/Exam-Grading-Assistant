import cv2
import numpy as np
from typing import List

class ImagePreprocessor:
    @staticmethod
    def preprocess(image_path: str, resize_dim: tuple = (800, 600)) -> np.ndarray:
        """
        Preprocess image for OCR
        - Resize
        - Convert to grayscale
        - Apply adaptive thresholding
        - Denoise
        """
        # Read image
        image = cv2.imread(image_path)
        
        # Resize
        image = cv2.resize(image, resize_dim, interpolation=cv2.INTER_AREA)
        
        # Convert to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # Adaptive thresholding
        thresh = cv2.adaptiveThreshold(
            gray, 255, 
            cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
            cv2.THRESH_BINARY, 11, 2
        )
        
        # Denoise
        denoised = cv2.fastNlMeansDenoising(thresh, None, 10, 7, 21)
        
        return denoised

    @staticmethod
    def batch_preprocess(image_paths: List[str]) -> List[np.ndarray]:
        """
        Preprocess multiple images
        """
        return [ImagePreprocessor.preprocess(path) for path in image_paths]
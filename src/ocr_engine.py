import os
import base64
import google.generativeai as genai
import numpy as np
import cv2
from typing import List

class OCREngine:
    def _init_(self):
        # Configure Gemini API
        genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
        
        # Initialize Gemini Pro Vision model
        self.model = genai.GenerativeModel('gemini-pro-vision')
    
    def extract_text(self, image_path: str) -> str:
        """
        Extract text from image using Gemini Vision API
        """
        try:
            # Read image
            image = cv2.imread(image_path)
            
            # Encode image to base64
            _, buffer = cv2.imencode('.jpg', image)
            image_base64 = base64.b64encode(buffer).decode('utf-8')
            
            # Prepare prompt for text extraction
            prompt = """
            Extract all readable text from this image. 
            Focus on handwritten or printed text. 
            If no text is visible, return an empty string.
            """
            
            # Generate content
            response = self.model.generate_content([
                prompt,
                {
                    'mime_type': 'image/jpeg',
                    'data': image_base64
                }
            ])
            
            return response.text.strip()
        
        except Exception as e:
            print(f"OCR Error: {e}")
            return ""
    
    def extract_batch_text(self, image_paths: List[str]) -> List[str]:
        """
        Extract text from multiple images
        """
        return [self.extract_text(path) for path in image_paths]
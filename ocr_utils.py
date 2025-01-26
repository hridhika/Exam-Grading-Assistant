'''import requests
import numpy as np
import pytesseract
from PIL import Image

# Function to send image to Gemini API for OCR processing
def extract_text_from_image(image_path, api_url, api_key):
    try:
        with open(image_path, 'rb') as image_file:
            files = {'file': image_file}
            headers = {'Authorization': f'Bearer {api_key}'}
            
            # Send the POST request to the API
            response = requests.post(api_url, files=files, headers=headers)

            if response.status_code == 200:
                extracted_text = response.json().get('text', '')
                return extracted_text
            else:
                print(f"Error: {response.status_code}")
                return None
    except Exception as e:
        print(f"Error during OCR: {e}")
        return None

# Alternative: Using Tesseract OCR if you prefer it over Gemini
def extract_text_tesseract_advanced(image_path):
    try:
        # OCR with custom configurations
        config = "--oem 3 --psm 6"  # Use LSTM OCR and treat image as a block of text
        text = pytesseract.image_to_string(Image.open(image_path), config=config)

        print("Extracted Text with Advanced Configurations:")
        print(text)
        return text
    except Exception as e:
        print("Error using advanced Tesseract:", e)
        return None

# Example usage
extract_text_tesseract_advanced(processed_path)

# Function to compute Word Error Rate (WER)
def calculate_wer(reference, hypothesis):
    reference = reference.split()
    hypothesis = hypothesis.split()
    
    # Create the Levenshtein distance matrix
    d = np.zeros((len(reference) + 1, len(hypothesis) + 1))

    for i in range(len(reference) + 1):
        d[i][0] = i
    for j in range(len(hypothesis) + 1):
        d[0][j] = j

    for i in range(1, len(reference) + 1):
        for j in range(1, len(hypothesis) + 1):
            cost = 0 if reference[i - 1] == hypothesis[j - 1] else 1
            d[i][j] = min(d[i - 1][j] + 1, d[i][j - 1] + 1, d[i - 1][j - 1] + cost)

    return d[len(reference)][len(hypothesis)]'''
from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
def extract_text_tesseract(image_path):
    try:
        # Perform OCR using Tesseract
        config = "--oem 3 --psm 6"  # LSTM-based OCR, treat as block of text
        text = pytesseract.image_to_string(Image.open(image_path), config=config)
        with open("text.txt","w") as file:
            file.write(text)

        print("Extracted Text:")
        print(text)
        return text
    except Exception as e:
        print(f"Error using Tesseract: {e}")
        return None

# Example usage
if __name__== "__main__":
    processed_image = "processed_image.jpg"
    extract_text_tesseract(processed_image)
'''from flask import Flask, render_template, request, jsonify
from ocr_utils import extract_text_from_image, calculate_wer

app = Flask(__name__)

# Replace with your Gemini API URL and API Key
API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=AIzaSyAKpV_mKPH_FrVH_R9jBygmRhIzoDtxCEk"  # Example URL
API_KEY = "AIzaSyAKpV_mKPH_FrVH_R9jBygmRhIzoDtxCEk"  # Replace with your actual API key

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Retrieve the uploaded image
        image_file = request.files["image"]
        image_path = image_file.filename
        image_file.save(image_path)

        # Extract text using Gemini OCR API
        extracted_text = extract_text_from_image(image_path, API_URL, API_KEY)

        # Example reference text (for WER calculation)
        reference_text = "This is a sample handwritten text"  # Replace with actual reference text
        
        # Calculate Word Error Rate (WER)
        if extracted_text:
            wer = calculate_wer(reference_text, extracted_text)
            return render_template("index.html", extracted_text=extracted_text, wer=wer)
        else:
            return render_template("index.html", error="OCR failed to extract text.")

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)'''

from image import preprocess_image
from ocr_utils import extract_text_tesseract
from grading import grade_answer

def main_workflow(input_image, output_image):
    # Step 1: Preprocess the image
    processed_image_path = preprocess_image(input_image, output_image)
    if not processed_image_path:
        print("Preprocessing failed.")
        return

    # Step 2: Perform OCR on the preprocessed image
    text = extract_text_tesseract(processed_image_path)
    if text:
        print("Final Extracted Text:")
        print(text)

        grade_percentage=grade_answer(reference_answer,text)
        print(f"Grading Result: {grade_percentage:.2f}% Correct")
    else:
        print("OCR failed to extract text.")

# Example usage
if __name__ == "__main__":
    input_image = "input_image.jpg"
    output_image = "processed_image.jpg"
    reference_answer = "Happy"
    main_workflow(input_image, output_image)
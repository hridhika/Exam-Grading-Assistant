#  EXAM GRADING ASSISTANT 🎯


## Basic Details
### Team Name: HORLICKS


### Team Members
- Member 1: Angelina Rose - TKMCE KOLLAM
- Member 2: Ann Maria Jose- TKMCE KOLLAM
- Member 3: Hridhika satheesh - TKMCE KOLLAM

### Hosted Project Link
[mention your project hosted project link here]

### Project Description
The Exam Grading Assistant is a web application that automates the evaluation of handwritten answer scripts. It uses image preprocessing and OCR (Optical Character Recognition) to extract text from scanned images, providing efficient and accurate text analysis for grading purposes.


### The Problem statement
Grading handwritten exams is a tedious and error-prone process, especially when deciphering illegible handwriting or managing large volumes of answer scripts. The Exam Grading Assistant solves this "critical issue" by automating text extraction, saving educators from squinting at messy handwriting and endless hours of manual grading!

### The Solution
We’re giving teachers their time (and sanity) back! The Exam Grading Assistant takes messy, handwritten answer sheets, sprinkles a bit of AI magic with image preprocessing and OCR, and delivers the extracted text on a silver platter. No more decoding hieroglyphics—just upload, process, and relax!

## Technical Details
### Technologies/Components Used
For Software:
Languages:-Python
HTML
CSS
JavaScript
- Frameworks used:Flask
- Libraries used:Pillow
OpenCV
PyTesseract
Tesseract-OCR
- Tools used:Google Chrome (or any browser for frontend testing)
Tesseract OCR Engine
Visual Studio Code (or any text editor/IDE)
Flask Development Server

For Hardware:
- [List main components]
- [List specifications]
- [List tools required]

### Implementation
For Software:

# Installation
sudo apt install python3 python3-pip         
python3 -m venv env                          
env\Scripts\activate                         
pip install flask pillow opencv-python pytesseract  
python app.py  

# Run
env\Scripts\activate                         # Activate virtual environment (Windows)
python app.py                                # Run the Flask app


### Project Documentation
For Software:

Name: Exam Grading Assistant
Purpose: Automates text extraction from handwritten answer scripts using OCR and preprocessing techniques.
Setup Instructions

Languages Used: Python, HTML, CSS, JavaScript
Frameworks: Flask
Libraries: Pillow, OpenCV, PyTesseract, Tesseract-OCR
Tools: Python, Tesseract OCR, Flask Development Server
Installation Commands:

bash
Copy
Edit
sudo apt install python3 python3-pip         # For Linux
brew install python                          # For macOS

python3 -m venv env                          # Create virtual environment
source env/bin/activate                      # Activate environment (Linux/macOS)
env\Scripts\activate                         # Activate environment (Windows)

pip install flask pillow opencv-python pytesseract  # Install required libraries

sudo apt install tesseract-ocr               # Install Tesseract (Linux)
brew install tesseract                       # Install Tesseract (macOS)
# For Windows, download and install Tesseract OCR from https://github.com/tesseract-ocr/tesseract
Run Instructions

Start Flask App:
bash
Copy
Edit
python app.py
Open Frontend: Open the HTML file in a browser or use Live Server.
Features

Accepts handwritten answer scripts as image files.
Preprocesses the images (resizing, enhancing contrast/brightness).
Extracts text using Optical Character Recognition (OCR).
Displays extracted text on the frontend for review.
File Structure

csharp
Copy
Edit
project/
│
├── app.py              # Flask backend
├── imagepre.py         # Image preprocessing logic
├── ocr_utils.py        # OCR utilities
├── uploads/            # Uploaded images
├── processed/          # Processed images
├── templates/
│   └── index.html      # Frontend HTML
└── static/             # Optional for CSS/JS
Testing

Upload a test image with handwritten text.
Check the extracted text displayed on the frontend.
Future Enhancements

Support for multiple languages in OCR.
Direct grading or evaluation of the extracted text.
Mobile app integration.


# Screenshots (Add at least 3)

![Screenshot1](Add screenshot 1 here with proper name)
*Add caption explaining what this shows*

![Screenshot2](Add screenshot 2 here with proper name)
*Add caption explaining what this shows*

![Screenshot3](Add screenshot 3 here with proper name)
*Add caption explaining what this shows*

# Diagrams
![Workflow](Add your workflow/architecture diagram here)
*Add caption explaining your workflow*

For Hardware:

# Schematic & Circuit
![Circuit](Add your circuit diagram here)
*Add caption explaining connections*

![Schematic](Add your schematic diagram here)
*Add caption explaining the schematic*

# Build Photos
![WhatsApp Image 2025-01-26 at 09 14 37_ecc1265a](https://github.com/user-attachments/assets/cad8bc88-707d-41db-b3d6-fe266864db55)




![Components](Add photo of your components here)
*List out all components shown*

![Build](Add photos of build process here)
*Explain the build steps*

![Final](Add photo of final product here)
*Explain the final build*

### Project Demo
# Video
[Add your demo video link here]
*Explain what the video demonstrates*

# Additional Demos
[Add any extra demo materials/links]

## Team Contributions
- [Name 1]: [Specific contributions]
- [Name 2]: [Specific contributions]
- [Name 3]: [Specific contributions]

---
Made with ❤️ at TinkerHub

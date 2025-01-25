import os
import uuid
from fastapi import FastAPI, File, UploadFile, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn
from dotenv import load_dotenv

# Import local modules
from src.grading_assistant import ExamGradingAssistant

# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI(title="Exam Grading Assistant")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Ensure upload directory exists
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Initialize grading assistant
grading_assistant = ExamGradingAssistant()

# Mount static files and templates
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.post("/upload")
async def upload_image(file: UploadFile = File(...)):
    try:
        # Generate unique filename
        filename = f"{uuid.uuid4()}_{file.filename}"
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        
        # Save file
        with open(filepath, "wb") as buffer:
            buffer.write(await file.read())
        
        # Grade the uploaded image
        results = grading_assistant.grade_exam([filepath])
        
        # Prepare response
        response = {
            'image_path': filename,
            'extracted_text': results[0]['extracted_text'],
            'reference_answer': results[0]['reference_answer'],
            'similarity_score': float(results[0]['similarity_score']),
            'is_correct': bool(results[0]['is_correct'])
        }
        
        return JSONResponse(content=response)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/results")
def read_results(request: Request):
    return templates.TemplateResponse("result.html", {"request": request})

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
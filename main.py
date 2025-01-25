import json
import os
from typing import Dict, List

from src.image_preprocessor import ImagePreprocessor
from src.ocr_engine import OCREngine
from src.semantic_analyzer import SemanticAnalyzer

class ExamGradingAssistant:
    def _init_(
        self, 
        reference_path='data/reference_answers.json', 
        similarity_threshold: float = 0.7
    ):
        # Load reference answers
        with open(reference_path, 'r') as f:
            self.reference_answers = json.load(f)
        
        self.preprocessor = ImagePreprocessor()
        self.ocr = OCREngine()
        self.semantic_analyzer = SemanticAnalyzer()
        self.threshold = similarity_threshold
    
    def grade_exam(self, image_paths: List[str]) -> List[Dict]:
        """
        Grade multiple exam answer images
        """
        # Preprocess images
        preprocessed_images = self.preprocessor.batch_preprocess(image_paths)
        
        # Extract text
        extracted_texts = self.ocr.extract_batch_text(preprocessed_images)
        
        # Grade each answer
        results = []
        for img_path, text in zip(image_paths, extracted_texts):
            # Find corresponding reference answer (assume filename is question ID)
            question_id = os.path.splitext(os.path.basename(img_path))[0]
            reference = self.reference_answers.get(question_id, "")
            
            # Calculate similarity
            similarity = self.semantic_analyzer.calculate_similarity(reference, text)
            
            results.append({
                'image_path': img_path,
                'extracted_text': text,
                'reference_answer': reference,
                'similarity_score': similarity,
                'is_correct': similarity >= self.threshold
            })
        
        return results
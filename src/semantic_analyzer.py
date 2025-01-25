import torch
from transformers import AutoTokenizer, AutoModel
from typing import List

class SemanticAnalyzer:
    def _init_(self, model_name='sentence-transformers/bert-base-nli-mean-tokens'):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModel.from_pretrained(model_name)
    
    def get_embedding(self, text: str) -> torch.Tensor:
        """
        Generate embedding for given text
        """
        inputs = self.tokenizer(
            text, 
            return_tensors='pt', 
            padding=True, 
            truncation=True, 
            max_length=512
        )
        
        with torch.no_grad():
            outputs = self.model(**inputs)
        
        # Mean pooling
        return torch.mean(outputs.last_hidden_state, dim=1).squeeze()
    
    def calculate_similarity(self, text1: str, text2: str) -> float:
        """
        Calculate cosine similarity between two texts
        """
        emb1 = self.get_embedding(text1)
        emb2 = self.get_embedding(text2)
        
        return torch.cosine_similarity(emb1, emb2, dim=0).item()
    
    def batch_similarity(self, reference: str, candidates: List[str]) -> List[float]:
        """
        Calculate similarities for multiple candidate answers
        """
        return [self.calculate_similarity(reference, candidate) for candidate in candidates]
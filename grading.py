from sentence_transformers import SentenceTransformer, util

# Function to load the extracted text from a file
def load_extracted_text(file_path):
    with open(file_path, 'r') as file:
        extracted_text = file.read().strip()
    return extracted_text

# Function to calculate similarity between reference and student's answers
def calculate_similarity_sbert(ref_answer, student_answer):
    model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
    emb1 = model.encode(ref_answer, convert_to_tensor=True)
    emb2 = model.encode(student_answer, convert_to_tensor=True)
    similarity = util.cos_sim(emb1, emb2).item()  # Compute cosine similarity
    return similarity

# Function to grade the answer based on similarity
def grade_answer(reference_answer, extracted_text):
    # Calculate similarity score
    similarity_score = calculate_similarity_sbert(reference_answer, extracted_text)

    # Convert similarity to percentage (assuming similarity score is between 0 and 1)
    grade_percentage = similarity_score * 100
    return grade_percentage

if __name__ == "__main__":
    # Reference answer (correct answer for comparison)
    reference_answer = "The capital of France is Paris."

    # Load the extracted text from the file
    extracted_text = load_extracted_text("extracted_text.txt")  # Ensure this file exists

    # Grade the answer and get percentage correctness
    grade_percentage = grade_answer(reference_answer, extracted_text)

    # Display the results
    print(f"Extracted Text: {extracted_text}")
    print(f"Similarity Score (Percentage Correctness): {grade_percentage:.2f}%")

import json
import os
import fitz  # PyMuPDF for PDF text extraction
import subprocess

# Function to extract text from a PDF
def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text("text")
    return text

def extract_resume_data_ollama(resume_text):
    prompt = f"""
    Extract structured information from this resume:
    all the skills 

    resume text:
    
    {resume_text}
    """

    # Running Ollama’s Llama 2 / Mistral model locally
    result = subprocess.run(
        ["ollama", "run", "llama2", prompt],
        capture_output=True,
        text=True
    )
    
    # Debugging: print stdout and stderr
    print("Ollama stdout:", result.stdout)
    print("Ollama stderr:", result.stderr)
    
    return result.stdout
    #try:
    #    return json.loads(result.stdout)  # Ensure it's valid JSON
    #except json.JSONDecodeError:
    #    print("Ollama response is not valid JSON. Returning raw text.")
    #    return {"raw_output": result.stdout}


"""
# Function to save all users' resumes into a single JSON file
def save_to_json(user_data, json_file="resumes.json"):
    if os.path.exists(json_file):
        with open(json_file, "r") as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                data = []
    else:
        data = []

    data.append(user_data)  # Append new user data

    with open(json_file, "w") as file:
        json.dump(data, file, indent=4)

    print(f"Data saved for {user_data.get('name', 'Unknown')}")
"""

# Function to save the extracted resume data into a text file formatted like a dictionary
def save_to_text(user_data, text_file="resumes.txt"):
    with open(text_file, "a") as file:  # Open in append mode to add new entries
        file.write(user_data + "\n\n")  # Write the raw dictionary-like string

    print(f"Data saved for resume")


# Main function to process a resume
def process_resume(pdf_path):
    resume_text = extract_text_from_pdf(pdf_path)
    resume_data = extract_resume_data_ollama(resume_text)
    #save_to_json(resume_data)
    save_to_text(resume_data)

# Example usage with an uploaded PDF
pdf_file = "resume1.pdf"
process_resume(pdf_file)

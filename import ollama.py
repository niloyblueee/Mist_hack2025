import ollama

def suggest_jobs_from_resume(resume_text):
    prompt = f"""
    Analyze the following resume text and extract key skills. Then, suggest 5 job roles that best match the person's skills and experience.

    Resume Text:
    {resume_text}

    Response format:
    - Extracted Skills: [list of skills]
    - Recommended Job Roles: [list of jobs]
    """

    response = ollama.chat(
        model="llama2",  # Use "mistral" if needed
        messages=[{"role": "user", "content": prompt}]
    )

    return response["message"]["content"].strip()

# Example usage
resume_text = "resumes.txt"

job_suggestions = suggest_jobs_from_resume(resume_text)
print(job_suggestions)
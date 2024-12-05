import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_mistralai import ChatMistralAI
from fastapi import FastAPI
from pydantic import BaseModel

load_dotenv()

app = FastAPI()
mistral_api_key = os.getenv("MISTRAL_API_KEY")

class JobOffer(BaseModel):
    text: str

class CV(BaseModel):
    text: str

@app.get("/")
async def root():
    return {"message": "API is running"}

@app.post("/analyze/")
async def analyze(job_offer: JobOffer, cv: CV):
    job_offer_data = extract_skills_and_experience(job_offer.text)
    cv_data = extract_skills_and_experience(cv.text)

    result = compare_cv_and_job_offer(cv_data, job_offer_data)

    review = generate_review(cv.text, job_offer.text, result)

    return {
        "review": review,
        "compatibilityScore": result["score"],
        "missingSkills": result["missing_skills"],
        "strengths": result["matching_skills"],
    }

def extract_skills_and_experience(text):
    llm = ChatMistralAI(
        model="mistral-large-latest",
        mistral_api_key=mistral_api_key,
        temperature=0,
        max_retries=2,
    )
    
    extraction_prompt = """
    Tu es un expert en RH. Analyse le texte suivant et extrait:
    1. Une liste de compétences techniques, qualifications et expertises
    2. Les années d'expérience si mentionnées
    
    Texte à analyser:
    {text}
    
    Retourne UNIQUEMENT un objet JSON valide dans ce format:
    {{"skills": ["skill1", "skill2", ...], "experience": "X years"}}
    """
    
    prompt = PromptTemplate(
        input_variables=["text"],
        template=extraction_prompt,
    )
    
    chain = prompt | llm
    result = chain.invoke(input={"text": text})
    
    try:
        response_text = str(result.content)
        if '```json' in response_text:
            response_text = response_text.split('```json\n')[1].split('```')[0]
        
        import json
        parsed_result = json.loads(response_text)
        print("Extracted data:", parsed_result)  # Debug
        return parsed_result
    except Exception as e:
        print(f"Extraction error: {e}")
        print(f"Raw extraction response: {result.content}")
        return {"skills": [], "experience": None}

# 2. ANALYSE DES CORRESPONDANCES
def compare_cv_and_job_offer(cv_data, job_offer_data):
    print("CV data:", cv_data)  # Debug
    print("Job offer data:", job_offer_data)  # Debug
    
    llm = ChatMistralAI(
        model="mistral-large-latest",
        mistral_api_key=mistral_api_key,
        temperature=0,
        max_retries=2,
    )
    
    comparison_prompt = """
    You are an HR expert. Compare these two sets of skills:

    Job Required Skills:
    {job_skills}

    Candidate Skills:
    {cv_skills}

    Return ONLY a valid JSON object in this format, with all information in French:
    {{
        "score": <note entre 0 et 100>,
        "matching_skills": ["compétence1", "compétence2"],
        "missing_skills": ["compétence3", "compétence4"]
    }}
    """
    
    prompt = PromptTemplate(
        input_variables=["job_skills", "cv_skills"],
        template=comparison_prompt,
    )
    
    chain = prompt | llm
    response = chain.invoke(input={
        "job_skills": job_offer_data["skills"],
        "cv_skills": cv_data["skills"]
    })
    
    try:
        response_text = str(response.content)
        if '```json' in response_text:
            response_text = response_text.split('```json\n')[1].split('```')[0]
        
        import json
        parsed_result = json.loads(response_text)
        print("Comparison result:", parsed_result)  # Debug
        return parsed_result
    except Exception as e:
        print(f"Comparison error: {e}")
        print(f"Raw comparison response: {response.content}")
        return {
            "score": 0,
            "matching_skills": [],
            "missing_skills": []
        }
# 3. REVUE QUALITATIVE UTILISANT GPT
def generate_review(cv, job_offer, result):
    llm = ChatMistralAI(
        model="mistral-large-latest",
        mistral_api_key=mistral_api_key,
        temperature=0,
        max_retries=2,
    )
    prompt_template = """
    Job offer:
    {job_offer}

    Candidate CV:
    {cv}

    Analysis results:
    - Score: {score}
    - Matching Skills: {matching_skills}
    - Missing Skills: {missing_skills}

    Please provide a detailed review of this candidate's compatibility with the job offer.
    Be concise and to the point write only in French.
    """
    prompt = PromptTemplate(
        input_variables=["job_offer", "cv", "score", "matching_skills", "missing_skills"],
        template=prompt_template,
    )
    
    chain = prompt | llm
    
    response = chain.invoke(input={
        "job_offer": job_offer,
        "cv": cv,
        "score": result["score"],
        "matching_skills": ", ".join(result["matching_skills"]),
        "missing_skills": ", ".join(result["missing_skills"])
    })
    
    return response


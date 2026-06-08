from fastapi import FastAPI
from pydantic import BaseModel
from groq import Groq
from dotenv import load_dotenv
import os


app=FastAPI()
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

class JDRequest(BaseModel):
    jd: str
    resume: str


@app.post("/analyze")
def analyze(request: JDRequest):
    prompt = f"""
    You are a resume analyzer.
    
    Job Description: {request.jd}
    Resume: {request.resume}
    
    Extract the skills required by the JD and check which ones are present in the resume.
    Return a JSON with:
    - matched_skills: list of skills in both JD and resume
    - missing_skills: list of skills required by JD but not in resume
    - match_score: percentage of matched skills
    - suggestion: one line advice to improve the resume


    Return ONLY a JSON object. No explanation, no code, no markdown. Just the raw JSON.
    """
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role":"user","content":prompt}]
    )

    return {"result": response.choices[0].message.content}
    

# JD Analyzer API

A REST API that analyzes how well your resume matches a job description using AI.

## Live API
Run locally — see instructions below.

## What it does
- Takes a job description and resume as input
- Sends them to Groq LLM for intelligent analysis
- Returns matched skills, missing skills, match score and a suggestion

## How it works
1. FastAPI receives the JD and resume via POST request
2. Sends them to Groq's Llama 3.1 model with a structured prompt
3. Returns the result as clean JSON

## Tech Stack
- Python
- FastAPI
- Groq API (Llama 3.1)
- python-dotenv

## How to run locally
1. Clone the repo
2. Install dependencies: `pip install fastapi uvicorn groq python-dotenv`
3. Create a `.env` file with your Groq API key: `GROQ_API_KEY=your_key_here`
4. Run: `python -m uvicorn main:app --reload`
5. Open: `http://localhost:8000/docs`
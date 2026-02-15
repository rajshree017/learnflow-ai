from fastapi import FastAPI
from pydantic import BaseModel
from ai_engine import generate_response
from prompts import tutor_prompt, roadmap_prompt, quiz_prompt, debug_prompt, docs_prompt
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS Fix
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class TutorRequest(BaseModel):
    topic: str

class RoadmapRequest(BaseModel):
    goal: str
    days: int

class QuizRequest(BaseModel):
    topic: str

class DebugRequest(BaseModel):
    issue: str

class DocsRequest(BaseModel):
    code: str

@app.post("/tutor")
def tutor(req: TutorRequest):
    prompt = tutor_prompt(req.topic, "English")
    output = generate_response(prompt)
    return {"answer": output}

@app.post("/roadmap")
def roadmap(req: RoadmapRequest):
    prompt = roadmap_prompt(req.goal, req.days, "English")
    output = generate_response(prompt)
    return {"answer": output}

@app.post("/quiz")
def quiz(req: QuizRequest):
    prompt = quiz_prompt(req.topic, "English")
    output = generate_response(prompt)
    return {"answer": output}

@app.post("/debug")
def debug(req: DebugRequest):
    prompt = debug_prompt(req.issue, "English")
    output = generate_response(prompt)
    return {"answer": output}

@app.post("/docs")
def docs(req: DocsRequest):
    prompt = docs_prompt(req.code, "English")
    output = generate_response(prompt)
    return {"answer": output}

@app.get("/")
def home():
    return {"message": "AI For Bharat - Backend is running!"}
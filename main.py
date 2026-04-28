from fastapi import FastAPI
from ai import get_ai_response

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Backend is running 🚀"}

@app.get("/ask")
def ask_ai(q: str):
    answer = get_ai_response(q)
    
    return {
        "question": q,
        "answer": answer,
        "status": "success"
    }
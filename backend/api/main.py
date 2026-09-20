from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from backend.rag.rag_pipeline import answer_question


app = FastAPI(title="PDF RAG Chatbot")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


class QuestionRequest(BaseModel):
    question: str


@app.get("/")
def root():
    return {"message": "PDF RAG Chatbot API is running"}


@app.post("/ask")
def ask_question(request: QuestionRequest):
    answer = answer_question(request.question)

    return {
        "question": request.question,
        "answer": answer
    }
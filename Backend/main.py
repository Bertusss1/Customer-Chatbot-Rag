from fastapi import FastAPI
from pydantic import BaseModel

from Chatbot import get_response

app = FastAPI()
from fastapi.middleware.cors import CORSMiddleware

class ChatRequest(BaseModel):
    session_id: str
    message: str


@app.get("/")
def home():
    return {
        "message": "Customer Service Chatbot"
    }


@app.post("/chat")
def chat(request: ChatRequest):

    reply = get_response(
        request.session_id,
        request.message
    )

    return {
        "reply": reply
    }

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
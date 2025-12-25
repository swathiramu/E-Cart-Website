from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from chatbot.chatbot import get_answer

app = FastAPI()

# CORS (Frontend → Backend connect aaga)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Static files serve panna
app.mount("/static", StaticFiles(directory="static"), name="static")

class ChatRequest(BaseModel):
    message: str

@app.get("/")
def root():
    return {"status": "Server running"}

@app.post("/chat")
def chat(req: ChatRequest):
    reply = get_answer(req.message)
    return {"reply": reply}

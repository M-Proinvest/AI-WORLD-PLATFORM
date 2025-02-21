from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Model danych do chatbota
class ChatRequest(BaseModel):
    message: str

@app.get("/")
def home():
    return {"message": "AI World Chatbot is running!"}

@app.get("/status")
def status():
    return {"status": "OK", "message": "System działa poprawnie"}

@app.post("/chat")
def chat(request: ChatRequest):
    user_message = request.message
    # Placeholder dla AI - tutaj dodamy OpenAI
    return {"response": f"Otrzymałem Twoją wiadomość: {user_message}"}

@app.post("/register")
def register():
    return {"message": "Rejestracja użytkownika (do wdrożenia)"}

@app.post("/login")
def login():
    return {"message": "Logowanie użytkownika (do wdrożenia)"}


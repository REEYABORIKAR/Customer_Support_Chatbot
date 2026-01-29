from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from chatbot.core.chatbot_engine import ChatbotEngine
from chatbot.config.setting import WELCOME_MESSAGE

app = FastAPI()
engine = ChatbotEngine()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "welcome": WELCOME_MESSAGE}
    )


@app.post("/chat")
async def chat(data: dict):
    user_message = data.get("message", "")
    bot_response = engine.process_message(user_message)

    if bot_response == "exit":
        return JSONResponse({"response": "Thank you for chatting with us. Goodbye!"})

    return JSONResponse({"response": bot_response})

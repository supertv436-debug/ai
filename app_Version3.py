from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

# Импортируйте свою AI-логику
# from my_source_code import my_ai_function

app = FastAPI()

# CORS — если фронтенд лежит на другом домене
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Статические файлы (frontend)
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def read_root():
    return FileResponse("static/index.html")  # Главная — ваш фронт

@app.post("/api/ask")
async def ask(request: Request):
    data = await request.json()
    question = data.get("question", "")

    # Вот тут вызывайте вашу АИ-логику, НЕ заглушка!
    # answer = my_ai_function(question)
    answer = logic_response(question)
    return {"answer": answer}

def logic_response(q: str):
    # Пример: используйте свою "умную" функцию
    # return my_ai_function(q)
    return "Ваш Python ассистент: " + q
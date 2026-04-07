from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import openai  # Если нужен OpenAI, иначе подключите свой AI

app = FastAPI()

# Разрешаем запросы с любых источников (для разработки)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Настройте ваш OpenAI API ключ, если используете
# openai.api_key = "YOUR_OPENAI_KEY"

@app.post("/api/ask")
async def ask(request: Request):
    data = await request.json()
    question = data.get("question", "")

    # Здесь интеграция с вашим AI-бэкендом:
    # Пример с OpenAI, замените на свой или усложните как надо

    # answer = call_my_true_ai_function(question)
    # return {"answer": answer}

    # Если OpenAI GPT:
    # response = openai.ChatCompletion.create(
    #     model="gpt-3.5-turbo",
    #     messages=[{"role": "user", "content": question}]
    # )
    # return {"answer": response["choices"][0]["message"]["content"]}

    # Пример простой обработки:
    answer = logic_response(question)
    return {"answer": answer}

def logic_response(question: str) -> str:
    # Реализуйте свою бизнес-логику или нейронку
    # Пока простой пример:
    if "привет" in question.lower():
        return "Здравствуйте! Как могу помочь?"
    # … тут ваша логика!
    return "Ответ ассистента: " + question
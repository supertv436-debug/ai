const form = document.getElementById('askForm');
const userInput = document.getElementById('userInput');
const responseDiv = document.getElementById('response');

form.addEventListener('submit', async (event) => {
    event.preventDefault();
    const question = userInput.value.trim();
    if (!question) return;
    responseDiv.textContent = 'Думаю...';

    try {
        const resp = await fetch('http://localhost:8000/api/ask', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({question}),
        });
        const data = await resp.json();
        if (data.answer) {
            responseDiv.textContent = data.answer;
        } else {
            responseDiv.textContent = "Нет ответа от ассистента.";
        }
    } catch (e) {
        responseDiv.textContent = "Ошибка при обращении к серверу.";
    }
    userInput.value = '';
});

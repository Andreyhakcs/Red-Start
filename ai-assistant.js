
async function getRecommendation() {
    const input = document.getElementById("userInput").value;
    const responseDiv = document.getElementById("response");

    if (!input) {
        responseDiv.innerText = "Пожалуйста, введите запрос.";
        return;
    }

    responseDiv.innerText = "Ищу лучшие предложения...";

    const result = await fetch("https://api.openai.com/v1/chat/completions", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Authorization": "Bearer YOUR_OPENAI_API_KEY"
        },
        body: JSON.stringify({
            model: "gpt-3.5-turbo",
            messages: [{ role: "user", content: `Найди мне ${input} по минимальной цене в Европе или Чехии. Используй краткие советы и рекомендации.` }]
        })
    });

    const data = await result.json();
    const message = data.choices?.[0]?.message?.content;
    responseDiv.innerText = message || "Ответа нет, проверь API-ключ или соединение.";
}

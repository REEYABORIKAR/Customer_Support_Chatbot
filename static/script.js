async function sendMessage() {
    const input = document.getElementById("user-input");
    const chatBox = document.getElementById("chat-box");

    if (!input.value.trim()) return;

    const userDiv = document.createElement("div");
    userDiv.className = "user-msg";
    userDiv.innerText = input.value;
    chatBox.appendChild(userDiv);

    const message = input.value;
    input.value = "";

    const response = await fetch("/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message })
    });

    const data = await response.json();

    const botDiv = document.createElement("div");
    botDiv.className = "bot-msg";
    botDiv.innerText = data.response;
    chatBox.appendChild(botDiv);

    chatBox.scrollTop = chatBox.scrollHeight;
}

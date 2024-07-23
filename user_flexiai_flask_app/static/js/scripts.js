// static/js/scripts.js
let threadId = null;

document.getElementById('send-button').addEventListener('click', sendMessage);
document.getElementById('message-input').addEventListener('keypress', function(event) {
    if (event.key === 'Enter') {
        sendMessage();
    }
});

function sendMessage() {
    const messageInput = document.getElementById('message-input');
    const message = messageInput.value.trim();
    if (message === '') return;

    console.log('Sending message:', message);

    // Add user message to chat directly without retrieval
    addMessage('You', message, 'user');

    // Send message to server
    fetch('/api/run', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: message, thread_id: threadId })
    })
    .then(response => response.json())
    .then(data => {
        console.log('Received response:', data); // Log the response to debug
        if (data.success) {
            threadId = data.thread_id;
            updateChat(data.messages);
        } else {
            addMessage('Error', 'Failed to get response from assistant.', 'error');
        }
    })
    .catch(error => {
        console.error('Fetch error:', error);
        addMessage('Error', 'An error occurred: ' + error.message, 'error');
    });

    // Clear input
    messageInput.value = '';
}

function addMessage(role, text, className) {
    console.log('Adding message:', role, text);

    const messageElement = document.createElement('li');
    messageElement.className = className;

    // Determine avatar based on role
    const avatar = role === 'You' ? '/static/images/user.png' : '/static/images/assistant.png';

    // Convert markdown to HTML
    try {
        const htmlContent = window.marked.parse(text);
        console.log('HTML Content:', htmlContent); // Log the HTML content to debug
        messageElement.innerHTML = `
            <div class="message-container">
                <div class="avatar"><img src="${avatar}" alt="${role}" /></div>
                <div class="message-content">
                    <div class="markdown-content">${htmlContent}</div>
                </div>
            </div>`;
    } catch (error) {
        console.error('Markdown conversion error:', error);
        messageElement.innerHTML = `
            <div class="message-container">
                <div class="avatar"><img src="${avatar}" alt="${role}" /></div>
                <div class="message-content">
                    <div class="markdown-content">${text}</div>
                </div>
            </div>`;
    }

    const messagesContainer = document.getElementById('messages');
    messagesContainer.appendChild(messageElement);
    messagesContainer.scrollTop = messagesContainer.scrollHeight;
}

function updateChat(messages) {
    messages.forEach(msg => {
        if (msg.role === 'Assistant') {
            addMessage('Assistant', msg.message, 'assistant');
        }
    });
}

// Test if marked is available
if (typeof window.marked !== 'undefined') {
    console.log('Marked library is loaded');
} else {
    console.error('Marked library is not loaded');
}

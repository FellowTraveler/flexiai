// static/js/scripts.js
let threadId = null;
let isProcessing = false;

document.getElementById('send-button').addEventListener('click', sendMessage);

const messageInput = document.getElementById('message-input');
messageInput.addEventListener('keydown', function(event) {
    if (event.key === 'Enter' && event.shiftKey) {
        const cursorPosition = this.selectionStart;
        const value = this.value;
        this.value = value.substring(0, cursorPosition) + "\n" + value.substring(cursorPosition);
        this.selectionStart = cursorPosition + 1;
        this.selectionEnd = cursorPosition + 1;
        event.preventDefault();
    } else if (event.key === 'Enter' && !event.shiftKey) {
        event.preventDefault();
        sendMessage();
    }
    autoResizeTextarea();
});

messageInput.addEventListener('input', autoResizeTextarea);

function autoResizeTextarea() {
    const maxRows = 10;
    const lineHeight = parseInt(window.getComputedStyle(messageInput).lineHeight);
    messageInput.style.height = '40px'; // Reset height to calculate new height
    const currentHeight = messageInput.scrollHeight;

    if (currentHeight > lineHeight * maxRows) {
        messageInput.style.height = (lineHeight * maxRows) + 'px';
        messageInput.style.overflowY = 'scroll';
    } else {
        messageInput.style.height = currentHeight + 'px';
        messageInput.style.overflowY = 'hidden';
    }
}

autoResizeTextarea();

function sendMessage() {
    const message = messageInput.value.trim();

    if (message === '') {
        alert('Message cannot be empty or whitespace.');
        return;
    }

    if (isProcessing) {
        alert('Please wait for the assistant to respond before sending a new message.');
        return;
    }

    addMessage('You', message, 'user', true);

    messageInput.value = '';
    autoResizeTextarea();

    isProcessing = true;

    fetch('/api/run', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: message, thread_id: threadId })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok ' + response.statusText);
        }
        return response.json();
    })
    .then(data => {
        if (data.success) {
            threadId = data.thread_id;
            updateChat(data.messages).then(() => {
                isProcessing = false;
                addCopyButtons();
            });
        } else {
            addMessage('Error', 'Failed to get response from assistant.', 'error');
            isProcessing = false;
        }
    })
    .catch(error => {
        console.error('Fetch error:', error);
        addMessage('Error', 'An error occurred: ' + error.message, 'error');
        isProcessing = false;
    });
}

function addMessage(role, text, className, isUserMessage = false) {
    const messageElement = document.createElement('div');
    messageElement.className = `message ${className}`;

    const avatar = role === 'You' ? '/static/images/user.png' : '/static/images/assistant.png';

    const formattedText = isUserMessage ? text.replace(/\n/g, '<br>') : text;

    try {
        const htmlContent = window.marked.parse(formattedText);
        messageElement.innerHTML = `
            <div class="message-container">
                <div class="avatar"><img src="${avatar}" alt="${role}"></div>
                <div class="message-content">
                    <div class="markdown-content">${htmlContent}</div>
                </div>
            </div>`;
    } catch (error) {
        console.error('Markdown conversion error:', error);
        messageElement.innerHTML = `
            <div class="message-container">
                <div class="avatar"><img src="${avatar}" alt="${role}"></div>
                <div class="message-content">
                    <div class="markdown-content">${formattedText}</div>
                </div>
            </div>`;
    }

    const messagesContainer = document.getElementById('messages');
    messagesContainer.appendChild(messageElement);
    messagesContainer.scrollTop = messagesContainer.scrollHeight;

    // Trigger MathJax to process any new LaTeX content
    if (window.MathJax) {
        MathJax.typesetPromise([messageElement]).catch(function (err) {
            console.error('MathJax error:', err.message);
        });
    }
}

function updateChat(messages) {
    return new Promise((resolve) => {
        messages.forEach(msg => {
            if (msg.role === 'Assistant') {
                addMessage('Assistant', msg.message, 'assistant');
            }
        });
        resolve();
    });
}

function addCopyButtons() {
    document.querySelectorAll('pre code').forEach((block) => {
        if (block.parentNode.querySelector('.copy-code-button')) {
            return;
        }
        const copyButton = document.createElement('button');
        copyButton.innerText = 'Copy';
        copyButton.className = 'copy-code-button';
        copyButton.addEventListener('click', () => {
            navigator.clipboard.writeText(block.innerText).then(() => {
                copyButton.innerText = 'Copied!';
                setTimeout(() => {
                    copyButton.innerText = 'Copy';
                }, 2000);
            });
        });
        const pre = block.parentNode;
        pre.style.position = 'relative';
        pre.insertBefore(copyButton, block);
    });
}

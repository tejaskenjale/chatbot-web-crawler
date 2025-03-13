import streamlit as st
import streamlit.components.v1 as components

# Enhanced Custom CSS with animations
custom_css = """
<style>
    #chat-button {
        position: fixed;
        bottom: 20px;
        right: 20px;
        z-index: 9999;
        transition: all 0.3s ease;
    }
    #chat-button button {
        background-color: #4CAF50;
        color: white;
        border: none;
        padding: 15px 32px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 25px;
        transition: all 0.3s ease;
    }
    #chat-button button:hover {
        background-color: #45a049;
        transform: scale(1.05);
    }
    #chat-popup {
        display: none;
        position: fixed;
        bottom: 90px;
        right: 20px;
        width: 300px;
        border: none;
        border-radius: 10px;
        background-color: white;
        box-shadow: 0 5px 35px rgba(0,0,0,0.2);
        z-index: 9999;
        transition: all 0.3s ease;
        opacity: 0;
        transform: translateY(20px);
    }
    #chat-popup.show {
        opacity: 1;
        transform: translateY(0);
    }
    #chat-messages {
        height: 300px;
        overflow-y: auto;
        padding: 15px;
        border-bottom: 1px solid #eee;
    }
    #chat-messages p {
        margin: 10px 0;
        line-height: 1.4;
        animation: fadeIn 0.5s ease;
    }
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    #chat-input {
        width: 100%;
        padding: 15px;
        border: none;
        border-top: 1px solid #eee;
        font-size: 14px;
        transition: all 0.3s ease;
    }
    #chat-input:focus {
        outline: none;
        box-shadow: 0 -5px 10px rgba(0,0,0,0.1);
    }
</style>
"""

# Enhanced JavaScript with smoother interactions
chat_script = """
<script>
function toggleChat() {
    var popup = document.getElementById("chat-popup");
    var button = document.getElementById("chat-button");
    if (popup.style.display === "none" || popup.style.display === "") {
        popup.style.display = "block";
        setTimeout(() => popup.classList.add("show"), 10);
        button.innerHTML = "<button>Close Chat</button>";
    } else {
        popup.classList.remove("show");
        setTimeout(() => popup.style.display = "none", 300);
        button.innerHTML = "<button>Chat</button>";
    }
}

function sendMessage() {
    var input = document.getElementById("chat-input");
    var message = input.value.trim();
    if (message) {
        addMessage("User", message);
        input.value = "";
        // Simulate typing indicator
        addTypingIndicator();
        // In a real app, you'd send this to the server
        setTimeout(() => {
            removeTypingIndicator();
            addMessage("Bot", "Thank you for your message. How can I assist you further?");
        }, 1500);
    }
}

function addMessage(sender, text) {
    var messages = document.getElementById("chat-messages");
    var messageElem = document.createElement("p");
    messageElem.innerHTML = "<strong>" + sender + ":</strong> " + text;
    messages.appendChild(messageElem);
    messages.scrollTop = messages.scrollHeight;
}

function addTypingIndicator() {
    var messages = document.getElementById("chat-messages");
    var indicatorElem = document.createElement("p");
    indicatorElem.id = "typing-indicator";
    indicatorElem.innerHTML = "<em>Bot is typing...</em>";
    messages.appendChild(indicatorElem);
    messages.scrollTop = messages.scrollHeight;
}

function removeTypingIndicator() {
    var indicator = document.getElementById("typing-indicator");
    if (indicator) indicator.remove();
}
</script>
"""

# HTML structure for the chat (unchanged)
chat_html = """
<div id="chat-button" onclick="toggleChat()">
    <button>Chat</button>
</div>
<div id="chat-popup">
    <div id="chat-messages"></div>
    <input type="text" id="chat-input" placeholder="Type a message..." onkeypress="if(event.key === 'Enter') sendMessage()">
</div>
"""

def main():
    st.set_page_config(page_title="KayJay AI Agent", layout="wide")

    st.title("Welcome to KayJay global solutions")
    st.write("Mission: - To empower businesses with innovative technology solutions that drive growth, efficiency, and positive impact.")

    # Combine all HTML, CSS, and JS
    full_html = f"{custom_css}{chat_script}{chat_html}"
    
    # Render the custom component
    components.html(full_html, height=600)

if __name__ == "__main__":
    main()

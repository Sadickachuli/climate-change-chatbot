import { useState, useEffect, useRef } from "react";
import axios from "axios";
import API_URL from "../config";
import "../styles.css";

const Chat = () => {
  const [userInput, setUserInput] = useState("");
  const [messages, setMessages] = useState<{ text: string; sender: string }[]>([]);
  const [loading, setLoading] = useState(false);
  const chatBoxRef = useRef<HTMLDivElement>(null);

  const sendMessage = async () => {
    if (!userInput.trim()) return;

    // Add user message to chat
    const newMessages = [...messages, { text: userInput, sender: "You" }];
    setMessages(newMessages);
    setUserInput("");
    setLoading(true);

    try {
      const response = await axios.post(`${API_URL}/chat`, { text: userInput });

      // Add bot response to chat
      setMessages([...newMessages, { text: response.data.response, sender: "Bot" }]);
    } catch (error) {
      console.error("Error fetching response:", error);
      setMessages([...newMessages, { text: "Error: Could not reach chatbot.", sender: "Bot" }]);
    }

    setLoading(false);
  };

  useEffect(() => {
    if (chatBoxRef.current) {
      chatBoxRef.current.scrollTop = chatBoxRef.current.scrollHeight;
    }
  }, [messages, loading]);

  return (
    <div className="chat-container">
      <div className="chat-header">Climate Change Chatbot</div>

      <div className="chat-box" ref={chatBoxRef}>
        {messages.map((msg, index) => (
          msg.sender === "You" ? (
            <div key={index} className="user-message">{msg.text}</div>
          ) : (
            <div key={index} className="bot-message-container">
              <img src="/cbotlog.png" alt="Bot" className="bot-avatar" />
              <div className="bot-message">{msg.text}</div>
            </div>
          )
        ))}

        {loading && (
          <div className="typing-indicator">
            <img src="/bot-avatar.png" alt="Bot" className="bot-avatar" />
            <div className="typing-dots">
              <span className="dot"></span>
              <span className="dot"></span>
              <span className="dot"></span>
            </div>
          </div>
        )}
      </div>

      <div className="input-area">
        <input
          type="text"
          placeholder="Ask about climate change..."
          value={userInput}
          onChange={(e) => setUserInput(e.target.value)}
          onKeyDown={(e) => e.key === "Enter" && sendMessage()}
        />
        <button onClick={sendMessage}>Send</button>
      </div>
    </div>
  );
};

export default Chat;

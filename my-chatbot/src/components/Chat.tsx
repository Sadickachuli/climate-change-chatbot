import { useState } from "react";
import axios from "axios";
import API_URL from "../config";
import "../styles.css"; // Import CSS for styling

const Chat = () => {
  const [userInput, setUserInput] = useState("");
  const [messages, setMessages] = useState<{ text: string; sender: string }[]>([]);
  const [loading, setLoading] = useState(false);

  const sendMessage = async () => {
    if (!userInput.trim()) return;

    // Add user message to chat
    const newMessages = [...messages, { text: userInput, sender: "You" }];
    setMessages(newMessages);
    setUserInput("");
    setLoading(true);

    try {
      const response = await axios.post(`${API_URL}/chat`, { text: userInput }); // ✅ FIXED HERE

      // Add bot response to chat
      setMessages([...newMessages, { text: response.data.response, sender: "Bot" }]);
    } catch (error) {
      console.error("Error fetching response:", error);
      setMessages([...newMessages, { text: "Error: Could not reach chatbot.", sender: "Bot" }]);
    }

    setLoading(false);
  };

  return (
    <div className="chat-container">
      <div className="chat-box">
        {messages.map((msg, index) => (
          <div key={index} className={msg.sender === "You" ? "user-message" : "bot-message"}>
            <strong>{msg.sender}:</strong> {msg.text}
          </div>
        ))}
        {loading && <div className="loading">Thinking...</div>}
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

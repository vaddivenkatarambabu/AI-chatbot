import { useState, useRef, useEffect } from "react";
import axios from "axios";
import "./styles/app.css"; // Make sure you have basic styling

function App() {
  const [message, setMessage] = useState("");
  const [chat, setChat] = useState([]);
  const chatEndRef = useRef(null);

  // Scroll to bottom when new message arrives
  useEffect(() => {
    chatEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [chat]);

  const sendMessage = async () => {
    if (!message.trim()) return;

    // Add user message to chat
    setChat((prev) => [...prev, { role: "user", content: message }]);

    try {
      // Send POST request to Flask backend
      const response = await axios.post("/chat", { message });

      const botReply = response.data?.data?.reply || response.data?.reply || "No response";
      setChat((prev) => [...prev, { role: "assistant", content: botReply }]);
    } catch (error) {
      console.error("Error:", error);
      setChat((prev) => [...prev, { role: "assistant", content: "Error: Could not get reply" }]);
    }

    setMessage("");
  };

  const handleKeyDown = (e) => {
    if (e.key === "Enter") {
      sendMessage();
    }
  };

  return (
    <div className="app-container p-6 max-w-lg mx-auto">
      <h1 className="text-2xl font-bold mb-4">AI Chatbot</h1>

      <div className="chat-window bg-gray-100 p-4 h-96 overflow-y-auto rounded-lg mb-4">
        {chat.map((msg, index) => (
          <div
            key={index}
            className={`my-2 ${msg.role === "user" ? "text-right text-blue-600" : "text-left text-green-700"}`}
          >
            <p><b>{msg.role === "user" ? "You" : "AI"}:</b> {msg.content}</p>
          </div>
        ))}
        <div ref={chatEndRef} />
      </div>

      <div className="flex gap-2">
        <input
          type="text"
          className="flex-1 border p-2 rounded-lg"
          placeholder="Type your message..."
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          onKeyDown={handleKeyDown}
        />
        <button
          className="bg-blue-600 text-white px-4 py-2 rounded-lg"
          onClick={sendMessage}
        >
          Send
        </button>
      </div>
    </div>
  );
}

export default App;

import { useEffect, useRef } from "react";

const ChatWindow = ({ chat }) => {
  const chatEndRef = useRef(null);

  // Scroll to bottom whenever chat changes
  useEffect(() => {
    chatEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [chat]);

  return (
    <div className="chat-window bg-gray-100 p-4 h-96 overflow-y-auto rounded-lg mb-4">
      {chat.map((msg, index) => (
        <div
          key={index}
          className={`my-2 ${
            msg.role === "user"
              ? "text-right text-blue-600"
              : "text-left text-green-700"
          }`}
        >
          <p>
            <b>{msg.role === "user" ? "You" : "AI"}:</b> {msg.content}
          </p>
        </div>
      ))}
      <div ref={chatEndRef} />
    </div>
  );
};

export default ChatWindow;

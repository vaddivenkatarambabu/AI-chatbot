import React from "react";

const MessageInput = ({ message, setMessage, onSend }) => {
  const handleKeyDown = (e) => {
    if (e.key === "Enter") {
      onSend();
    }
  };

  return (
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
        className="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700"
        onClick={onSend}
      >
        Send
      </button>
    </div>
  );
};

export default MessageInput;

import React, { useState } from 'react';
import ChatBox from './components/ChatBox.jsx';
import ChatInput from './components/ChatInput.jsx';

const App = () => {
  const [messages, setMessages] = useState([]);

  const handleSend = async (message) => {
    const newMessage = { type: 'user', text: message };
    setMessages((prev) => [...prev, newMessage]);

    try {
      const res = await fetch('http://localhost:8000/api/chat-groq', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message }),
      });

      const data = await res.json();

      console.log(message)
      setMessages((prev) => [...prev, { type: 'bot', text: data.response || 'No response' }]);
    } catch (err) {
      setMessages((prev) => [...prev, { type: 'bot', text: '⚠️ Error talking to bot' }]);
    }
  };

  return (
    <div className="chat-container">
      <div className="chat-box">
        {messages.map((msg, index) => (
          <ChatBox key={index} message={msg} />
        ))}
      </div>
      <ChatInput onSend={handleSend} />
    </div>
  );
};

export default App;

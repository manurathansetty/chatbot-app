import React, { useEffect, useState } from 'react';
import ChatBox from './components/ChatBox.jsx';
import ChatInput from './components/ChatInput.jsx';
import ThunderField from './components/ThunderField.jsx';
import './components/index.css';

const App = () => {
  const [messages, setMessages] = useState([]);
  const API_URL = 'https://chatbot-app-ozjv.onrender.com/api/chat-groq';

  const handleSend = async (message) => {
    const newMessage = { type: 'user', text: message };
    setMessages((prev) => [...prev, newMessage]);

    try {
      const res = await fetch(API_URL, {
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

  // Fetch a welcome message from the backend once on mount
  useEffect(() => {
    const getWelcome = async () => {
      try {
        const welcomePrompt = 'Hello';
        const res = await fetch(API_URL, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ message: welcomePrompt }),
        });
        const data = await res.json();
        setMessages((prev) => [
          { type: 'bot', text: data.response || 'Welcome! How can I help you today?' },
          // ...prev,
        ]);
      } catch (e) {
        console.log("Error", e.body)
      }
    };
    getWelcome();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  return (
    <div className="chat-container theme-dark">
      <ThunderField />
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

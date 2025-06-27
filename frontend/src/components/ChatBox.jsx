import React from 'react';
import './index.css'

const ChatBox = ({ message }) => {
  return (
    <div className={`message ${message.type}`}>
      <p>{message.text}</p>
    </div>
  );
};

export default ChatBox;

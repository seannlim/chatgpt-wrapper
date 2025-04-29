// frontend/src/App.js

import React, { useState } from 'react';
import './App.css';

function App() {
  const [message, setMessage] = useState('');
  const [reply, setReply] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();

    const response = await fetch('http://127.0.0.1:5001/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message }),
    });

    const data = await response.json();
    setReply(data.reply);
  };

  return (
    <div className="App">
      <h1>My ChatGPT Wrapper</h1>
      <form onSubmit={handleSubmit}>
        <input 
          type="text" 
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          placeholder="Ask me anything..." 
        />
        <button type="submit">Send</button>
      </form>
      <div className="response">
        <p><strong>Reply:</strong> {reply}</p>
      </div>
    </div>
  );
}

export default App;

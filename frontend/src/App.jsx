import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from './assets/vite.svg'
import heroImg from './assets/hero.png'
import './App.css'

function App() {
  return (
    <div className="app">
      <div className="chat-container">
        <div className="chat-header">
          <h1>AI Assistant</h1>
        </div>

        <div className="messages">
          <div className="message bot">
            Hello! Ask me anything.
          </div>
        </div>

        <div className="input-area">
          <input
            type="text"
            placeholder="Ask anything..."
          />

          <button>
            Send
          </button>
        </div>
      </div>
    </div>
  );
}

export default App;

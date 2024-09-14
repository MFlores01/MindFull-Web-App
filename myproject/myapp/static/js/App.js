// App.js
import React, { useState } from 'react';
import styled from 'styled-components';
import Navbar from './Navbar';
import Sidebar from './Sidebar';
import ContactButtons from './ContactButtons';
import Messages from './Messages';

const MainContainer = styled.div`
  width: 1440px;
  height: 1024px;
  position: relative;
  background: white;
  box-shadow: 0px 0px 15px rgba(0, 0, 0, 0.25);
  border-radius: 30px;
  overflow: hidden;
`;

const AppContainer = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
`;

const App = () => {
  const [inputMessage, setInputMessage] = useState('');
  const [messages, setMessages] = useState([]);

  const handleSendMessage = () => {
    if (inputMessage.trim() !== '') {
      setMessages([...messages, inputMessage]);
      setInputMessage('');
    }
  };

  return (
    <AppContainer>
      <h1> Hello </h1>
      <MainContainer>
        <Navbar />
        <Sidebar />
        <ContactButtons />
        <Messages newMessages={messages} />
        <div>
          <input
            type="text"
            value={inputMessage}
            onChange={(e) => setInputMessage(e.target.value)}
          />
          <button onClick={handleSendMessage}>Send</button>
        </div>
      </MainContainer>
    </AppContainer>
  );
};

export default App;

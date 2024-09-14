// Messages.js
import React from 'react';
import styled from 'styled-components';

const MessagesContainer = styled.div`
  width: calc(100% - 505px);
  height: 100%;
  position: absolute;
  top: 0;
  right: 0;
  padding: 20px;
  overflow-y: auto;
`;

const MessageContainer = styled.div`
  width: 609px;
  height: 330px;
  position: relative;
`;

const MessageContent = styled.div`
  width: 262px;
  height: 50px;
  left: 0;
  top: 280px;
  position: absolute;
`;

const Group3 = styled.div`
  width: 197px;
  height: 44px;
  left: 65px;
  top: 3px;
  position: absolute;
`;

const Rectangle6 = styled.div`
  width: 197px;
  height: 44px;
  left: 0;
  top: 0;
  position: absolute;
  background: #696969;
  border-radius: 30px;
`;

const MessageText = styled.div`
  left: 18px;
  top: 11px;
  position: absolute;
  color: white;
  font-size: 16px;
  font-family: 'Open Sans';
  font-weight: 700;
  word-wrap: break-word;
`;

const Image4 = styled.img`
  width: 50px;
  height: 50px;
  left: 0;
  top: 0;
  position: absolute;
  border-radius: 100px;
`;

const Message = ({ content }) => (
  <MessageContainer>
    <MessageContent>
      <Group3>
        <Rectangle6 />
        <MessageText>{content}</MessageText>
      </Group3>
      <Image4 src="https://via.placeholder.com/50x50" alt="User" />
    </MessageContent>
  </MessageContainer>
);

const Messages = ({ newMessages }) => {
  return (
    <MessagesContainer>
      {newMessages.map((message, index) => (
        <Message key={index} content={message} />
      ))}
    </MessagesContainer>
  );
};

export default Messages;

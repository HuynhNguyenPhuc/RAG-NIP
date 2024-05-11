import { useState } from "react";
import "./App.css";
import "@chatscope/chat-ui-kit-styles/dist/default/styles.min.css";
import {
 MainContainer,
 ChatContainer,
 MessageList,
 Message,
 MessageInput,
 TypingIndicator,
} from "@chatscope/chat-ui-kit-react";

function App() {
  const [isChatbotTyping, setIsChatbotTyping] = useState(false);

  const [chatMessages, setChatMessages] = useState([
    {
      message: "Hello, I am Chatbot!",
      sender: "Chatbot",
      direction: "incoming",
      position: "single"
    },
  ]);

  const handleUserMessage = async (userMessage) => {
    const newUserMessage = {
      message: userMessage,
      sender: "user",
      direction: "outgoing",
      position: "single"
    };

    const updatedChatMessages = [...chatMessages, newUserMessage];
    setChatMessages(updatedChatMessages);

    setIsChatbotTyping(true);
    await processUserMessageToChatbot(userMessage);
  };


  async function processUserMessageToChatbot(message) {
    await fetch("http://127.0.0.1:8000/recommends", {
      method: "POST",
      headers: {
          "Content-Type": "application/json",
      },
      body: JSON.stringify({
          sentence: message
      })
    })
      .then((data) => {
        return data.json();
      })
      .then((data) => {
        setChatMessages([
          ...chatMessages,
          {
            message: processOutput(data["paper"], data["recommend"]),
            sender: "Chatbot",
            direction: "incoming",
            position: "single"
          },
        ]);
        setIsChatbotTyping(false);
      });
    }

    function convertStringList(string) {
      const trimmedString = string.slice(1, -1);
      const items = trimmedString.split(", ");
      for (let i = 0; i < items.length; i++) {
          items[i] = items[i].slice(1, -1);
      }
      const result = items.join(', ');
      return result;
    }

    const processOutput = (paper, recommendedPapers) => {
      let output = `Paper:\nTitle: ${paper.title}\nAuthor: ${convertStringList(paper.author)}\n\nRecommendations:\n`;
      recommendedPapers.forEach(recommendedPaper => {
        output += `Title: ${recommendedPaper.title}\nAuthor: ${convertStringList(recommendedPaper.author)}\n\n`;
      });
      return output;
    };
  

  return (
    <>
      <div style={{ position: "relative", height: "100vh", width: "700px" }}>
        <MainContainer>
          <ChatContainer>
            <MessageList
              typingIndicator={
                isChatbotTyping ? (
                  <TypingIndicator content="Chatbot is thinking" />
                ) : null
              }
            >
              {chatMessages.map((message, i) => {
                return (
                  <Message
                    key={i}
                    model={message}
                    style={
                      message.sender === "Chatbot" ? { textAlign: "left" } : {}
                    }
                  />
                );
              })}
            </MessageList>
            <MessageInput
              placeholder="Type message here"
              onSend={handleUserMessage}
            />
          </ChatContainer>
        </MainContainer>
      </div>
    </>
 );
}

export default App;
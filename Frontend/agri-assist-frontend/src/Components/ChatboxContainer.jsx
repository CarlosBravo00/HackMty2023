import React, { useState, useEffect } from "react";
import { postData } from '../Services/apicalls.js'
import "./style.css";

export const ChatBoxContainer = () => {
  const [userInput, setUserInput] = useState("");
  const [response, setResponse] = useState("");
  const [isLoading, setIsLoading] = useState(false);

  const handleUserInput = (e) => {
    setUserInput(e.target.value);
  };

  const handleSend = () => {
    setIsLoading(true); // Show loading animation while processing

    postData(userInput)
      .then(data => {
        console.log(data)
        setResponse(data.response); // Set the response received from the server
        setIsLoading(false); // Hide loading animation
      })
      .catch(error => {
        console.error('There was an error!', error);
        setResponse('Error occurred while processing your request.'); // You might want to set a user-friendly error message
        setIsLoading(false); // Hide loading animation
      });
  };


  useEffect(() => {
    // You can add any logic here to handle user input and generate responses
  }, [userInput]);

  return (
    <div className="ChatBoxContainer" style={{ marginRight: 150 }}>
      <div className="rectangle">
        <div className="intro-container">
          <img src="/icon.png" alt="Icon" className="icon" />
          <p style={{ marginLeft: 20 }}>Hello I´m AgroLisa, Im here to help you...</p>
        </div>
        {isLoading ? (
          <p>Loading...</p>
        ) : (
          <div className="response">
            <p>{response}</p>
          </div>
        )}
        <div className="input-container">
          <input
            type="text"
            placeholder="Type your question here..."
            value={userInput}
            onSubmit={handleSend}
            onChange={handleUserInput}
          />

          <button disabled={isLoading} style={{ backgroundColor: 'green', color: 'white', fontSize: '16px', padding: '10px', borderRadius: '20px', width: '200px', marginTop: '15px', cursor: 'pointer' }} onClick={handleSend}>Send
          </button>
        </div>
      </div>
    </div>
  );
};

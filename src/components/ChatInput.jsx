import React, { useState, useEffect, useRef } from "react";
import {
  ToggleLeftIcon,
  ToggleRightIcon,
  Mic,
  SendIcon,
  Copy,
} from "lucide-react";
import axios from "axios";

const ChatInterface = ({ onMessageSent }) => {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [isToggleOn, setIsToggleOn] = useState(false);
  const [isLoading, setIsLoading] = useState(false);
  const messagesEndRef = useRef(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(scrollToBottom, [messages]);

  const getIpAddress = async () => {
    try {
      const response = await fetch("https://httpbin.org/ip");
      const data = await response.json();
      return data.origin;
    } catch (error) {
      console.error("Error fetching IP address:", error);
      return "Unknown";
    }
  };

  const handleSendMessage = async () => {
    if (!input.trim()) {
      console.error("Input is empty.");
      return;
    }

    const userMessage = { role: "user", content: input };
    setMessages((prev) => [...prev, userMessage]);
    setInput("");
    setIsLoading(true);

    // Hide Welcome component when message is sent
    onMessageSent();

    try {
      // Fetch the user's IP address
      const userIp = await getIpAddress();

      // Send the POST request to the API
      const response = await axios.post(
        "https://9ae5-117-96-43-108.ngrok-free.app/rag/siva/query",
        {
          user_query: input.trim(),
          user_ip: userIp,
          db_name: "SIH",
          collection_name: "pdfs",
        },
        {
          headers: {
            "Content-Type": "application/json",
          },
          withCredentials: true, // Optional: Only if cookies/session are used
        }
      );

      // Extract the response data
      const data = response.data;

      // Append the assistant's response to the chat messages
      const assistantMessage = {
        role: "assistant",
        content: data.response || "No response received.",
      };
      setMessages((prev) => [...prev, assistantMessage]);
    } catch (error) {
      console.error("Error sending message:", error);

      // Append a default error message if the request fails
      const errorMessage = {
        role: "assistant",
        content: "Sorry, I could not process your request.",
      };
      setMessages((prev) => [...prev, errorMessage]);
    } finally {
      setIsLoading(false);
    }
  };

  const handleKeyPress = (e) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      handleSendMessage();
    }
  };

  const toggleSwitch = () => {
    setIsToggleOn((prev) => !prev);
  };

  const copyToClipboard = (text) => {
    navigator.clipboard.writeText(text).then(
      () => alert("Message copied to clipboard!"),
      (err) => console.error("Failed to copy text: ", err)
    );
  };

  return (
    <div className="flex flex-col h-full w-full chat-interface">
      <div className="flex-1 overflow-y-auto p-4 space-y-4 mb-16">
        <div className="max-w-4xl mx-auto w-full px-4 pt-24">
          {messages.map((message, index) => (
            <div
              key={index}
              className={`flex ${
                message.role === "user" ? "justify-end" : "justify-start"
              } mb-4`}
            >
              <div
                className={`message-container pl-4 pr-4 pt-1 pb-1 rounded-xl max-w-[60%] ${
                  message.role === "user"
                    ? "bg-purple-900 text-white ml-8 h-[80%] flex items-center font-semibold"
                    : " text-WHITE mr-8"
                }`}
              >
                {message.content}
                <button
                  onClick={() => copyToClipboard(message.content)}
                  className="absolute bottom-2 right-2 p-1 bg-gray-700 rounded-full text-white hover:bg-gray-600"
                >
                  <Copy className="w-5 h-5" />
                </button>
              </div>
            </div>
          ))}
          {isLoading && (
            <div className="relative">
              <span className="w-[10px] h-[10px] bg-[#FFFFFF] rounded-full absolute top-0 left-0 animate-blink"></span>
              <span className="w-[10px] h-[10px] bg-[#FFFFFF] rounded-full absolute top-0 left-0 animate-blink delay-200 ml-[15px]"></span>
              <span className="w-[10px] h-[10px] bg-[#FFFFFF] rounded-full absolute top-0 left-0 animate-blink delay-400 ml-[30px]"></span>
            </div>
          )}
          <div ref={messagesEndRef} />
        </div>
      </div>

      <div className="fixed bottom-0 w-full p-4 flex justify-center">
        <div className="relative w-1/2 max-w-2xl min-w-[320px]">
          <div className="absolute left-4 top-1/2 -translate-y-1/2">
            <div className="w-6 h-6 rounded-full bg-gradient-to-r from-blue-500 to-purple-500 flex items-center justify-center">
              <span className="text-xs text-white font-bold">S</span>
            </div>
          </div>
          <input
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={handleKeyPress}
            placeholder="Ask Siva.AI..."
            disabled={isLoading}
            className="w-full p-4 pl-12 pr-40 rounded-lg border border-gray-300 dark:border-gray-700 bg-black dark:bg-black text-gray-900 dark:text-gray-100 disabled:opacity-60"
          />
          <div className="absolute right-2 top-1/2 -translate-y-1/2 flex items-center space-x-2">
            {/* <button
              onClick={toggleSwitch}
              className="p-2 hover:bg-gray-100 dark:hover:bg-gray-700 rounded-full"
            >
              {isToggleOn ? (
                <ToggleRightIcon className="w-10 h-7 text-green-500" />
              ) : (
                <ToggleLeftIcon className="w-10 h-7 text-gray-500" />
              )}
            </button>
            <button
              className="p-2 hover:bg-gray-100 dark:hover:bg-gray-700 rounded-full"
              disabled={isLoading}
            >
              <Mic className="w-8 h-6 text-gray-500" />
            </button> */}
            <button
              onClick={handleSendMessage}
              disabled={!input.trim() || isLoading}
              className="p-2 hover:bg-gray-100 dark:hover:bg-gray-700 rounded-full disabled:opacity-50"
            >
              <SendIcon className="w-6 h-6 text-white" />
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ChatInterface;

import React, { useState, KeyboardEvent } from 'react';
import { ToggleLeftIcon, ToggleRightIcon, Mic, SendIcon } from 'lucide-react';

const ChatInput = () => {
  const [input, setInput] = useState('');
  const [isToggleOn, setIsToggleOn] = useState(false); // State for toggle switch

  const handleKeyPress = (e: KeyboardEvent<HTMLInputElement>) => {
    if (e.key === 'Enter' && input.trim()) {
      handleSend();
    }
  };

  const handleSend = () => {
    if (input.trim()) {
      console.log('Sending message:', input);
      setInput('');
    }
  };

  const toggleSwitch = () => {
    setIsToggleOn((prev) => !prev);
    console.log('Toggle State:', isToggleOn ? 'Off' : 'On');
  };

  return (
    <div className="fixed bottom-4 left-72 right-4">
      <div className="max-w-4xl mx-auto relative">
        <div className="absolute left-4 top-1/2 -translate-y-1/2">
          <div className="w-6 h-6 rounded-full bg-gradient-to-r from-blue-500 to-purple-500 flex items-center justify-center">
            <span className="text-xs text-white font-bold">S</span>
          </div>
        </div>
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyPress={handleKeyPress}
          placeholder="Ask Siva.AI..."
          className="w-full p-4 pl-14 pr-40 rounded-lg border border-gray-300 dark:border-gray-700 bg-white dark:bg-gray-800 text-gray-900 dark:text-gray-100"
        />
        <div className="absolute right-2 top-1/2 -translate-y-1/2 flex items-center space-x-2">
          {/* Toggle Button with Hover Effect */}
          <div className="relative group">
            <button
              onClick={toggleSwitch}
              className="p-2 hover:bg-gray-100 dark:hover:bg-gray-700 rounded-full"
            >
              {isToggleOn ? (
                <ToggleRightIcon className="w-10 h-7 text-green-500" />
              ) : (
                <ToggleLeftIcon className="w-10 h-7 text-gray-500" />
              )}
            </button>
            {/* Hover Text */}
            <span  className="absolute up-9 down-7 -translate-x-14 bg-gray-200 text-gray-900 dark:bg-gray-600 dark:text-white px--3 py--6 rounded-md text-sm shadow-md opacity-0 group-hover:opacity-100 transition-opacity duration-900 bottom: 40px">
            Complex
            </span>
          </div>
          <button className="p-2 hover:bg-gray-100 dark:hover:bg-gray-700 rounded-full">
            <Mic className="w-8 h-6 text-gray-500" />
          </button>
          <button className="p-2 hover:bg-gray-100 dark:hover:bg-gray-700 rounded-full">
            <SendIcon className="w-6 h-6 text-gray-500" />
          </button>
        </div>
      </div>
    </div>
  );
};

export default ChatInput;

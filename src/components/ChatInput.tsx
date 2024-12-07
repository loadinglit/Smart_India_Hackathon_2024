import React, { useState, KeyboardEvent } from 'react';
import { Paperclip, Mic, Send, Sparkles, Share2 } from 'lucide-react';

const ChatInput = () => {
  const [input, setInput] = useState('');

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
          <button className="p-2 hover:bg-gray-100 dark:hover:bg-gray-700 rounded-full">
            <Paperclip className="w-5 h-5 text-gray-500" />
          </button>
          <button className="p-2 hover:bg-gray-100 dark:hover:bg-gray-700 rounded-full">
            <Sparkles className="w-5 h-5 text-gray-500" />
          </button>
          <button className="p-2 hover:bg-gray-100 dark:hover:bg-gray-700 rounded-full">
            <Mic className="w-5 h-5 text-gray-500" />
          </button>
         {/* <button className="p-2 hover:bg-gray-100 dark:hover:bg-gray-700 rounded-full">
            <Share2 className="w-5 h-5 text-gray-500" />
          </button>
          <button 
            onClick={handleSend}
            className="p-2 bg-blue-600 hover:bg-blue-700 rounded-full transition-colors"
          >
            <Send className="w-5 h-5 text-white" />
          </button> */}
        </div>
      </div>
    </div>
  );
};

export default ChatInput;
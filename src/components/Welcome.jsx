import React from "react";
import {
  Phone,
  MessageSquare,
  DownloadIcon,
  DownloadCloud,
  DownloadCloudIcon,
  MoveDownIcon,
  ArrowDownCircle,
} from "lucide-react";

const Welcome = () => {
  return (
    <div className="flex flex-col items-start max-w-4xl mx-auto mt-8">
      <div className="w-16 h-16 relative mb-6">
        <div className="absolute inset-0 bg-gradient-to-r from-blue-500 via-purple-500 to-pink-500 rounded-full animate-pulse"></div>
        <div className="absolute inset-1 bg-white dark:bg-gray-900 rounded-full flex items-center justify-center">
          <div className="text-1xl font-bold bg-gradient-to-r from-blue-600 to-purple-600 text-transparent bg-clip-text">
            Siva.AI
          </div>
        </div>
      </div>

      <h1 className="text-7xl font-bold mb-4">
        <span className="bg-gradient-to-r from-blue-600 via-purple-600 to-pink-600 text-transparent bg-clip-text">
          Hello, Bhoomika
        </span>
      </h1>
      <p className="text-2xl text-gray-700 dark:text-gray-400 mb-8">
        How can I help your enterprise level query today? <br />I can help you
        extract, summarize, create reports & more.
      </p>

      <div className="flex flex-wrap gap-4">
        <button className="flex items-center px-6 py-3 bg-blue-500 text-white rounded-lg hover:bg-blue-400 transition-colors">
          Explore Chatbots, Prompts & Features
          <ArrowDownCircle className="w-7 h-5 mr-0" />
        </button>
        {/* <button className="flex items-center px-6 py-3 bg-blue-500 text-white rounded-lg hover:bg-blue-600 transition-colors">
          <Phone className="w-5 h-5 mr-2" />
          Get Siva.AI on Call
        </button> */}
      </div>
    </div>
  );
};

export default Welcome;

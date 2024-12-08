import React, { useState, useEffect } from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Navbar from "./components/Navbar";
import Sidebar from "./components/Sidebar";
import Welcome from "./components/Welcome";
import ChatHistory from "./components/ChatHistory";
import ChatInput from "./components/ChatInput";
import KnowledgeBase from "./components/KnowledgeBase";
import DataManagement from "./components/DataManagement";

function App() {
  const [darkMode, setDarkMode] = useState(false);

  useEffect(() => {
    if (darkMode) {
      document.documentElement.classList.add("dark");
    } else {
      document.documentElement.classList.remove("dark");
    }
  }, [darkMode]);

  const toggleDarkMode = () => {
    setDarkMode(!darkMode);
  };

  return (
    <Router>
      <div className="min-h-screen bg-gray-50 dark:bg-gray-900 transition-colors duration-200">
        <Navbar />
        <Sidebar darkMode={darkMode} toggleDarkMode={toggleDarkMode} />
        <main className="ml-64 pt-16 px-8">
          <Routes>
            <Route path="/" element={<Welcome />} />
            <Route path="/chats" element={<ChatHistory />} />
            <Route path="/knowledge-hub" element={<KnowledgeBase />} />
            <Route path="/datamanagement" element={<DataManagement />} />
            {/* Add more routes as needed */}
          </Routes>
          <ChatInput />
        </main>
      </div>
    </Router>
  );
}

export default App;

import React, { useState, useEffect } from 'react';
import Navbar from './components/Navbar';
import Sidebar from './components/Sidebar';
import Welcome from './components/Welcome';
import ChatHistory from './components/ChatHistory';
import ChatInput from './components/ChatInput';

function App() {
  const [darkMode, setDarkMode] = useState(false);

  useEffect(() => {
    if (darkMode) {
      document.documentElement.classList.add('dark');
    } else {
      document.documentElement.classList.remove('dark');
    }
  }, [darkMode]);

  const toggleDarkMode = () => {
    setDarkMode(!darkMode);
  };

  return (
    <div className="min-h-screen bg-gray-50 dark:bg-gray-900 transition-colors duration-200">
      <Navbar />
      <Sidebar darkMode={darkMode} toggleDarkMode={toggleDarkMode} />
      <main className="ml-64 pt-16 px-8">
        <Welcome />
        <ChatHistory />
        <ChatInput />
      </main>
    </div>
  );
}

export default App;
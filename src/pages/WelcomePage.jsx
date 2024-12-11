import React from "react";
import Navbar from "../components/Navbar";
import Sidebar from "../components/Sidebar";
import Welcome from "../components/Welcome";
import ChatInput from "../components/ChatInput";
import { useState , useEffect } from "react";
function WelcomePage(){

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
    return(
        <div>
            <Navbar />
            <Sidebar darkMode={darkMode} toggleDarkMode={toggleDarkMode} />
            <Welcome />
            <ChatInput />
        </div>
    )
}

export default WelcomePage;
import React from "react";
import Navbar from "../components/Navbar";
import Sidebar from "../components/Sidebar";
import Welcome from "../components/Welcome";
import ChatInput from "../components/ChatInput";
import { useState , useEffect } from "react";
import SparkleEffect from "../components/SparkleEffect";
import ParticlesBackground from "../components/ParticlesBackground";
function WelcomePage(){

    const [darkMode, setDarkMode] = useState(false);

    useEffect(() => {
      if (darkMode) {
        document.documentElement.classList.remove("dark");
      } else {
        document.documentElement.classList.add("dark");
      }
    }, [darkMode]);
  
    const toggleDarkMode = () => {
      setDarkMode(!darkMode);
    };
    return(
        <div>
            <Navbar />
            <ParticlesBackground/>

            <Sidebar darkMode={darkMode} toggleDarkMode={toggleDarkMode} />
            <Welcome />
            <ChatInput />

        </div>
    )
}

export default WelcomePage;
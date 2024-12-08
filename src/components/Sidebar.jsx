import React from "react";
import { useNavigate } from "react-router-dom";
import {
  Home,
  MessageSquare,
  Users,
  BookOpen,
  Store,
  Sun,
  Moon,
  LogOut,
  Plus,
  MessageCircle,
} from "lucide-react";

const Sidebar = ({ darkMode, toggleDarkMode }) => {
  const navigate = useNavigate();

  const menuItems = [
    { icon: Home, text: "Home", path: "/" },
    { icon: MessageSquare, text: "Chats", path: "/chats" },
    { icon: Users, text: "Teams", path: "/teams" },
    { icon: BookOpen, text: "Knowledge Hub", path: "/knowledge-hub" },
    { icon: BookOpen, text: "Data Management", path: "/datamanagement" },
    { icon: Store, text: "Agent Store", path: "/store" },
  ];

  return (
    <div className="fixed left-0 top-16 h-[calc(100vh-4rem)] w-64 bg-gray-50 dark:bg-gray-900 p-4 flex flex-col border-r border-gray-200 dark:border-gray-700">
      <button className="w-full bg-black dark:bg-white text-white dark:text-black rounded-lg p-3 flex items-center justify-center mb-6">
        <Plus className="w-5 h-5 mr-2" />
        New Chat
      </button>

      <div className="flex-1">
        {menuItems.map((item, index) => (
          <button
            key={index}
            className="w-full text-left p-3 rounded-lg mb-2 flex items-center hover:bg-gray-200 dark:hover:bg-gray-800"
            onClick={() => navigate(item.path)}
          >
            <item.icon className="w-5 h-5 mr-3 text-gray-600 dark:text-gray-300" />
            <span className="text-gray-700 dark:text-gray-200">
              {item.text}
            </span>
          </button>
        ))}
      </div>

      <div className="mt-auto border-t border-gray-200 dark:border-gray-700 pt-4">
        <button className="w-full text-left p-3 rounded-lg mb-2 flex items-center hover:bg-gray-200 dark:hover:bg-gray-800">
          <MessageCircle className="w-5 h-5 mr-3 text-gray-600 dark:text-gray-300" />
          <span className="text-gray-700 dark:text-gray-200">Feedback</span>
        </button>
        <button
          onClick={toggleDarkMode}
          className="w-full text-left p-3 rounded-lg mb-2 flex items-center hover:bg-gray-200 dark:hover:bg-gray-800"
        >
          {darkMode ? (
            <>
              <Sun className="w-5 h-5 mr-3 text-gray-600 dark:text-gray-300" />
              <span className="text-gray-700 dark:text-gray-200">
                Light Mode
              </span>
            </>
          ) : (
            <>
              <Moon className="w-5 h-5 mr-3 text-gray-600 dark:text-gray-300" />
              <span className="text-gray-700 dark:text-gray-200">
                Dark Mode
              </span>
            </>
          )}
        </button>
        <button className="w-full text-left p-3 rounded-lg mb-2 flex items-center hover:bg-gray-200 dark:hover:bg-gray-800">
          <LogOut className="w-5 h-5 mr-3 text-gray-600 dark:text-gray-300" />
          <span className="text-gray-700 dark:text-gray-200">Log Out</span>
        </button>
      </div>
    </div>
  );
};

export default Sidebar;

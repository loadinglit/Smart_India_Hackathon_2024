import React from 'react';
import { Link, useLocation } from 'react-router-dom';
import { Book, Database } from 'lucide-react';

const Sidebar = () => {
  const location = useLocation();

  const navItems = [
    { name: 'Knowledge Base', href: '/', icon: Book },
    { name: 'Data Management', href: '/data-management', icon: Database },
  ];

  return (
    <div className="w-64 bg-gray900 h-screen p-4 shadow-md">
      <h1 className="text-2xl font-bold mb-8 text-white">Admin Panel</h1>
      <nav>
        {navItems.map((item) => (
          <Link
            key={item.name}
            to={item.href}
            className={`flex items-center space-x-2 mb-4 p-2 rounded-lg ${
              location.pathname === item.href
                ? "bg-blue-500 text-white"
                : "text-white hover:bg-white hover:text-black"
            }`}
          >
            <item.icon className="h-5 w-5" />
            <span>{item.name}</span>
          </Link>
        ))}
      </nav>
    </div>
  );
};

export default Sidebar;


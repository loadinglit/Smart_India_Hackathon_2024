import React, { useState } from "react";
import { Youtube, FileText, Link, FileSpreadsheet } from "lucide-react";
import { useSpring, animated } from "@react-spring/web";

const AnimatedContainer = ({ isVisible, children }) => {
  const animation = useSpring({
    opacity: isVisible ? 1 : 0,
    maxHeight: isVisible ? 1000 : 0,
    overflow: "hidden",
  });

  return <animated.div style={animation}>{children}</animated.div>;
};

const KnowledgeBaseForm = () => {
  const [activeInput, setActiveInput] = useState(null);
  const [showUrlButtons, setShowUrlButtons] = useState(false);
  const [urlMode, setUrlMode] = useState(null);

  const inputFields = [
    { name: "youtubeUrl", icon: Youtube, label: "YouTube URL" },
    { name: "pdfFile", icon: FileText, label: "Upload PDF" },
    { name: "websiteUrl", icon: Link, label: "Website URL" },
    { name: "excelFile", icon: FileSpreadsheet, label: "Upload Excel" },
  ];

  return (
    <div className="min-h-screen bg-black text-white flex justify-center items-center p-6">
      <form className="bg-gray-900 p-8 rounded-lg shadow-lg w-full max-w-3xl space-y-5">
        {/* Heading */}
        <h1 className="text-2xl font-bold text-center text-[#B026FF] mb-4">
          Knowledge Base Form
        </h1>

        {/* Input Options */}
        <div className="grid grid-cols-1 sm:grid-cols-2 gap-6">
          {inputFields.map((field) => (
            <div
              key={field.name}
              className="bg-gray-800 p-4 rounded-lg shadow-md cursor-pointer flex flex-col items-center justify-center transition-all duration-300 hover:shadow-lg hover:bg-[#B026FF]"
              onClick={() => {
                setActiveInput(field.name);
                setShowUrlButtons(field.name === "websiteUrl");
              }}
            >
              <field.icon className="w-10 h-10 text-[#B026FF]" />
              <h3 className="text-lg font-semibold mt-2">{field.label}</h3>
            </div>
          ))}
        </div>

        {/* Animated Input Section */}
        <AnimatedContainer isVisible={activeInput !== null}>
          <div className="bg-gray-800 p-6 rounded-lg shadow-md">
            {activeInput === "youtubeUrl" && (
              <div>
                <label className="block text-sm font-medium mb-2">YouTube URL</label>
                <input
                  type="url"
                  placeholder="Enter YouTube URL"
                  className="w-full px-4 py-2 bg-gray-700 border border-gray-600 rounded-md focus:ring-2 focus:ring-[#B026FF]"
                />
                <button className="mt-4 w-full bg-[#B026FF] py-2 rounded-lg text-white hover:bg-purple-800">
                  Submit
                </button>
              </div>
            )}

            {activeInput === "websiteUrl" && showUrlButtons && (
              <div>
                <div className="flex gap-4 mb-4">
                  <button
                    type="button"
                    onClick={() => setUrlMode("single")}
                    className="w-full py-2 bg-gray-700 rounded-lg hover:bg-[#B026FF] border border-gray-600 text-sm"
                  >
                    Single URL
                  </button>
                  <button
                    type="button"
                    onClick={() => setUrlMode("crawling")}
                    className="w-full py-2 bg-gray-700 rounded-lg hover:bg-[#B026FF] border border-gray-600 text-sm"
                  >
                    Crawling
                  </button>
                </div>

                <input
                  type="url"
                  placeholder="Enter Website URL"
                  className="w-full px-4 py-2 bg-gray-700 border border-gray-600 rounded-md focus:ring-2 focus:ring-[#B026FF] mb-4"
                />

                {urlMode === "crawling" && (
                  <input
                    type="number"
                    placeholder="Enter Crawl Depth"
                    className="w-full px-4 py-2 bg-gray-700 border border-gray-600 rounded-md focus:ring-2 focus:ring-[#B026FF] mb-4"
                  />
                )}

                <button className="mt-4 w-full bg-[#B026FF] py-2 rounded-lg text-white hover:bg-purple-800">
                  Submit
                </button>
              </div>
            )}
          </div>
        </AnimatedContainer>
      </form>
    </div>
  );
};

export default KnowledgeBaseForm;

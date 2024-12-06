import React, { useState } from 'react';
import { useSpring, animated } from 'react-spring';
import { Youtube, FileText, Link } from 'lucide-react';

const AnimatedContainer = ({ isVisible, children }) => {
  const animation = useSpring({
    opacity: isVisible ? 1 : 0,
    maxHeight: isVisible ? 1000 : 0,
    overflow: 'hidden',
  });

  return <animated.div style={animation}>{children}</animated.div>;
};

const KnowledgeBaseForm = () => {
  const [formData, setFormData] = useState({
    youtubeUrl: '',
    pdfFile: null,
    websiteUrl: '',
    excludeDomains: '',
    excludeKeywords: '',
    limit: '',
  });

  const [message, setMessage] = useState("");
  const [activeInput, setActiveInput] = useState(null);
  const [showUrlButtons, setShowUrlButtons] = useState(false);
  const [selectedOption, setSelectedOption] = useState(null); // Store which button is selected for website URL

  const handleInputChange = (e) => {
    const { name, value, files } = e.target;
    setFormData((prev) => ({
      ...prev,
      [name]: files ? files[0] : value,
    }));
  };

  const handleYouTubeSubmit = async () => {
    if (!formData.youtubeUrl) {
      setMessage("Please enter a valid YouTube URL.");
      return;
    }

    try {
      const response = await fetch("http://localhost:8000/youtube/process-channel/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ channel_handle: formData.youtubeUrl }),
      });

      const data = await response.json();
      setMessage(data.message || "YouTube URL processed successfully.");
    } catch (error) {
      console.log(error);
      setMessage("An error occurred while processing the YouTube URL.");
    }
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (activeInput === 'youtubeUrl') {
      handleYouTubeSubmit();
    } else {
      console.log('Form submitted:', formData);
    }
  };

  const inputFields = [
    { name: 'youtubeUrl', icon: Youtube, label: 'YouTube URL', type: 'url', placeholder: 'Enter YouTube URL' },
    { name: 'pdfFile', icon: FileText, label: 'PDF Upload', type: 'file', accept: '.pdf' },
    { name: 'websiteUrl', icon: Link, label: 'Website URL', type: 'url', placeholder: 'Enter website URL' },
  ];

  return (
    <form onSubmit={handleSubmit} className="space-y-6">
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        {inputFields.map((field) => (
          <div
            key={field.name}
            className="bg-white p-6 rounded-lg shadow-md cursor-pointer transition-all duration-300 hover:shadow-lg"
            onClick={() => {
              setActiveInput(field.name);
              if (field.name === 'websiteUrl') {
                setShowUrlButtons(true);
              } else {
                setShowUrlButtons(false);
              }
            }}
          >
            <div className="flex items-center justify-center">
              <field.icon className="w-8 h-8 text-blue-500" />
            </div>
            <h3 className="text-lg font-semibold text-center mt-2">{field.label}</h3>
          </div>
        ))}
      </div>

      <AnimatedContainer isVisible={activeInput !== null}>
        <div className="bg-white p-6 rounded-lg shadow-md mt-6">
          {inputFields.map((field) => (
            <AnimatedContainer key={field.name} isVisible={activeInput === field.name}>
              <div className="mb-4">
                <label htmlFor={field.name} className="block text-sm font-medium text-gray-700 mb-2">
                  {field.label}
                </label>

                <div className="flex items-center space-x-4">
                  <input
                    type={field.type}
                    id={field.name}
                    name={field.name}
                    accept={field.accept}
                    placeholder={field.placeholder}
                    value={field.name === 'youtubeUrl' ? formData.youtubeUrl : formData.websiteUrl}
                    onChange={handleInputChange}
                    className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                  />

                  {field.name === 'youtubeUrl' && (
                    <button
                      type="button"
                      onClick={handleYouTubeSubmit}
                      className="bg-blue-500 text-white py-2 px-6 rounded-md hover:bg-blue-600 transition duration-300 ml-4"
                    >
                      Submit
                    </button>
                  )}
                </div>

                {field.name === 'youtubeUrl' && message && (
                  <p className="mt-4 text-sm text-green-500">{message}</p>
                )}
              </div>

              {/* Render buttons for Website URL */}
              {field.name === 'websiteUrl' && showUrlButtons && (
                <div className="space-x-4 mb-6">
                  <button
                    type="button"
                    onClick={() => setSelectedOption('singleUrl')}
                    className="bg-blue-500 text-white py-2 px-6 rounded-md hover:bg-blue-600 transition duration-300"
                  >
                    Single URL
                  </button>
                  <button
                    type="button"
                    onClick={() => setSelectedOption('crawl')}
                    className="bg-blue-500 text-white py-2 px-6 rounded-md hover:bg-blue-600 transition duration-300"
                  >
                    Crawl
                  </button>
                </div>
              )}

              {/* Render input fields based on the selected button */}
              {selectedOption && (
                <div className="space-y-4">
                  <div>
                    <label htmlFor="excludeDomains" className="block text-sm font-medium text-gray-700 mb-2">
                      Exclude Domains
                    </label>
                    <input
                      type="text"
                      id="excludeDomains"
                      name="excludeDomains"
                      value={formData.excludeDomains}
                      onChange={handleInputChange}
                      className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                    />
                  </div>

                  <div>
                    <label htmlFor="excludeKeywords" className="block text-sm font-medium text-gray-700 mb-2">
                      Exclude Keywords
                    </label>
                    <input
                      type="text"
                      id="excludeKeywords"
                      name="excludeKeywords"
                      value={formData.excludeKeywords}
                      onChange={handleInputChange}
                      className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                    />
                  </div>

                  {selectedOption === 'crawl' && (
                    <div>
                      <label htmlFor="limit" className="block text-sm font-medium text-gray-700 mb-2">
                        Limit
                      </label>
                      <input
                        type="number"
                        id="limit"
                        name="limit"
                        value={formData.limit}
                        onChange={handleInputChange}
                        className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                      />
                    </div>
                  )}
                </div>
              )}
            </AnimatedContainer>
          ))}
        </div>
      </AnimatedContainer>
    </form>
  );
};

export default KnowledgeBaseForm;

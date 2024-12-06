import React, { useState } from "react";

function App() {
  const [channelHandle, setChannelHandle] = useState("");
  const [message, setMessage] = useState("");
  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);

  // YouTube Channel Processor Handler
  const handleYoutubeSubmit = async (event) => {
    event.preventDefault();
    try {
      const response = await fetch(
        "http://localhost:8000/youtube/process-channel/",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ channel_handle: channelHandle }),
        }
      );

      const data = await response.json();
      setMessage(data.message);
    } catch (error) {
      setMessage("An error occurred.");
    }
  };

  // PDF File Upload Handler
  const handleFileChange = (e) => {
    const selectedFile = e.target.files[0];
    if (selectedFile && selectedFile.type === "application/pdf") {
      setFile(selectedFile);
    } else {
      alert("Please select a valid PDF file.");
    }
  };

  const handlePdfUpload = async () => {
    if (!file) {
      alert("Please select a file.");
      return;
    }

    setLoading(true);
    setMessage(""); // Clear previous messages

    const formData = new FormData();
    formData.append("pdf_file", file, file.name);

    try {
      const response = await fetch("http://localhost:8000/pdf/process-pdfs", {
        // Note the /pdf/ prefix
        method: "POST",
        body: formData,
      });

      if (!response.ok) {
        const errorText = await response.text();
        throw new Error(errorText || "Error processing PDF file");
      }

      const data = await response.json();
      setMessage(data.message);
    } catch (error) {
      console.error("Upload error:", error);
      setMessage(error.message || "Error processing PDF file");
    } finally {
      setLoading(false);
    }
  };
  return (
    <div>
      <h1>YouTube Channel Processor</h1>
      <form onSubmit={handleYoutubeSubmit}>
        <label>
          Enter YouTube Channel Handle:
          <input
            type="text"
            value={channelHandle}
            onChange={(e) => setChannelHandle(e.target.value)}
          />
        </label>
        <button type="submit">Process Channel</button>
      </form>

      <hr />

      <h1>Upload PDF for Processing</h1>
      <input type="file" onChange={handleFileChange} accept="application/pdf" />
      <button onClick={handlePdfUpload} disabled={loading}>
        {loading ? "Uploading..." : "Upload PDF"}
      </button>

      <hr />

      {message && <p>{message}</p>}
    </div>
  );
}

export default App;

import React, { useState } from "react";
import axios from "axios";

const App = () => {
  const [cropDetails, setCropDetails] = useState(null);
  const [error, setError] = useState(null);

  const fetchCropDetails = async () => {
    try {
      const response = await axios.post("http://localhost:3000/api/cropDetails", {
        cropName: "Rice",
      });

      setCropDetails(response.data);
      setError(null); // Clear errors
    } catch (err) {
      console.error("Error fetching crop details:", err);
      setError(err.response ? err.response.data : "An error occurred");
    }
  };

  const renderData = (data) => {
    // Convert the nested JSON into React components
    return Object.entries(data).map(([key, value]) => (
      <div key={key} style={{ marginLeft: "20px" }}>
        <h1>{key}:</h1>
        {typeof value === "object" ? (
          <div style={{ marginLeft: "20px" }}>
            {renderData(value)}
          </div>
        ) : (
          <h3>{value}</h3>
        )}
      </div>
    ));
  };

  return (
    <div>
      <button onClick={fetchCropDetails}>Get Rice Details</button>

      {error && <p style={{ color: "red" }}>{error.error || "Error occurred"}</p>}

      {cropDetails && (
        <div>
          {Object.entries(cropDetails).map(([cropName, cropData]) => (
            <div key={cropName}>
              <h1>{cropName}:</h1>
              <div style={{ marginLeft: "20px" }}>{renderData(cropData)}</div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default App;

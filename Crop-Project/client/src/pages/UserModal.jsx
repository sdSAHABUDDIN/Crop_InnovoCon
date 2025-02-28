import React, { useState } from "react";


const UserModal = ({ onSubmit }) => { // Accept onSubmit as a prop
  const [cityName, setCityName] = useState("");
  const [farm, setFarm] = useState("");
  const [language,setLanguage]=useState("")

  

  const handleSubmit = async() => { // No need to destructure here
    if (!onSubmit || typeof onSubmit !== "function") {
      console.error("Error: onSubmit is not a function!");
      return;
    }
    try{
      const url = `https://api.openweathermap.org/data/2.5/weather?q=${cityName}&appid=3926a46d705147093e15a749aba16c28`;
      //3926a46d705147093e15a749aba16c28
      const response=await fetch(url);
      const data=await response.json();
      console.log(data)
      const kelvinToCelsius = (temp) => (temp - 273.15).toFixed(2); // Convert Kelvin to Celsius
      const kelvinToFahrenheit = (temp) => ((temp - 273.15) * 9/5 + 32).toFixed(2); // Convert Kelvin to Fahrenheit
      const weatherData = {
        humidity: data.main.humidity,
        windSpeed: data.wind.speed,
        temperature: kelvinToCelsius(data.main.temp), 
        maxTemp: kelvinToCelsius(data.main.temp_max),
        minTemp: kelvinToCelsius(data.main.temp_min),
        location: data.name,
      };
      if (cityName && farm) {
        const prompt = `I am from ${cityName}. I want to do ${farm} farming. Our weather conditions: Max temperature is ${weatherData.maxTemp}°C, and Min temperature is ${weatherData.minTemp}°C. Please help me find the best way to make money.give me ans in ${language}`;
        console.log(prompt)
        console.log("onSubmit function:",onSubmit)
        onSubmit({weatherData,farm,cityName,prompt}); // Call onSubmit function with user data
        console.log("onSubmit function:",onSubmit)
      } else {
        alert("Please fill all details!");
      }
    }catch(error){
      console.log("Error fetching weather data", error);
    }
    
  };

  return (
    <div className="fixed top-0 left-0 w-full h-full flex items-center justify-center bg-black bg-opacity-50">
      <div className="bg-white p-6 rounded-lg shadow-lg">
        <h2 className="text-xl font-bold mb-4">Enter Your Details</h2>
        <input
          type="text"
          placeholder="Enter your city Name"
          value={cityName}
          onChange={(e) => setCityName(e.target.value)}
          className="border p-2 w-full mb-2"
        />
        <input
          type="text"
          placeholder="what kind of farming you want ot do?"
          value={farm}
          onChange={(e) => setFarm(e.target.value)}
          className="border p-2 w-full mb-2"
        />
        <input
          type="text"
          placeholder="In which language would you like to receive the answer?"
          value={language}
          onChange={(e) => setLanguage(e.target.value)}
          className="border p-2 w-full mb-2"
        />
        <button
          onClick={handleSubmit}
          className="bg-blue-500 text-white px-4 py-2 rounded"
        >
          Submit
        </button>
      </div>
    </div>
  );
};

export default UserModal;

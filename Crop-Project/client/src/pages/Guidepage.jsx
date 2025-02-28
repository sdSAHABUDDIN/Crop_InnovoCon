import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { Crop } from '../contant';
import axios from 'axios';

const GuidCard = ({ crop }) => {
  const navigate = useNavigate();
  const handleCardClick = async () => {
  try {
    // Fetch crop details from the backend
    const response = await axios.post('http://localhost:5000/api/cropDetails', {
      cropName: crop.name.toLowerCase(), // Send lowercase crop name
    });
    
    // Navigate to crop details page with the fetched data
    navigate('/guide', { state: { cropName: crop.name, details: response.data } });
  } catch (error) {
    console.error('Error fetching crop details:', error);
    alert(error.response?.data?.error || 'Crop not found or server error.');
  }
};
  return (
    <div 
    onClick={handleCardClick}
    className="bg-[#1a1a1a] bg-opacity-80 rounded-lg shadow-lg cursor-pointer w-[300px] h-[400px] flex flex-col items-center justify-center">
      {/* Dynamic crop image */}
      <div
        className="relative bg-cover bg-center w-[250px] h-[150px] rounded-lg"
        style={{ backgroundImage: `url(${crop.img})` }}
      />
      <h2 className="mt-4 text-lg font-semibold text-white">{crop.name}</h2>
      <h2 className="px-4 sm:px-10 py-10">
        Click
      </h2>
    </div>
  );
};

const Guidepage = () => {
  const [searchText, setSearchText] = useState(''); // State to store search text

  // Filter crops based on search text
  const filteredCrops = Crop.filter((crop) =>
    crop.name.toLowerCase().includes(searchText.toLowerCase())
  );

  return (
    <>
      {/* Heading */}
      <h1 className="text-3xl sm:text-4xl font-bold text-black px-4 sm:px-10 py-10">
        Learn How to Cultivate Your Favorite Crops Step by Step!
      </h1>
      

      {/* Search Input with custom placeholder color */}
      <div className="flex justify-center items-center flex-col py-4 px-4 sm:px-10">
        <input
          type="text"
          placeholder="Search for a crop (e.g., Apple)"
          className="w-full bg-slate-600 sm:w-[400px] px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-red-500 placeholder-red-300"
          value={searchText}
          onChange={(e) => setSearchText(e.target.value)} // Update search text
        />
        <p className="px-4 mt-4 sm:px-10 text-gray-300">
        Click on a crop to discover its cultivation process.
      </p>
      </div>
      

      {/* Crop Grid */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6 px-4 sm:px-10 py-10">
        {filteredCrops.length > 0 ? (
          filteredCrops.map((crop) => <GuidCard key={crop.name} crop={crop} />)
        ) : (
          <p className="text-center text-gray-400 col-span-full">
            No crops found matching "{searchText}".
          </p>
        )}
      </div>
    </>
  );
};

export default Guidepage;

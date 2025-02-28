import React from 'react';
import { useLocation } from 'react-router-dom';

const Guide = () => {
  const location = useLocation();
  const { cropName, details } = location.state || {};
  
  const normalizedCropName = cropName?.toLowerCase();
  const cropDetails = details?.[normalizedCropName];
  console.log('Crop Name:', cropName);
  console.log('Details:', details);
  console.log('Normalized Crop Name:', normalizedCropName);
  console.log('Crop Details:', cropDetails);
  if (!cropDetails) {
    return (
      <div className="text-center text-red-500 mt-10">
        <h1 className="text-2xl font-bold">No Details Available</h1>
        <p>Please try selecting another crop.</p>
      </div>
    );
  }
  return (
    <div className="px-4 sm:px-10 py-10">
    <h1 className="text-3xl sm:text-4xl font-bold text-green-500">
      {cropName} Cultivation Details
    </h1>
    <div className="mt-6 bg-[#1a1a1a] p-6 rounded-lg shadow-lg">
      {Object.entries(cropDetails).map(([section, steps]) => (
        <div key={section} className="mb-6">
          <h2 className="text-2xl text-yellow-300 font-semibold mb-2">
            {section.replace(/_/g, ' ')}
          </h2>
          <ul className="list-disc list-inside text-gray-300">
            {Object.entries(steps).map(([stepNo, stepDescription]) => (
              <li key={stepNo}>
                Step {stepNo}: {stepDescription}
              </li>
            ))}
          </ul>
        </div>
      ))}
    </div>
  </div>
);
};

export default Guide;

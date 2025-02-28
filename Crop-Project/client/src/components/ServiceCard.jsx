import React from 'react';
import { useNavigate } from 'react-router-dom';
import { Tilt } from 'react-tilt';
import { motion } from 'framer-motion';
import PropTypes from 'prop-types';
import axios from 'axios';
// FactorCard component for rendering environmental details
const FactorCard = ({ icon, label, value }) => (
  <div className="w-[80px] flex flex-col items-center">
    <img
      src={icon}
      alt={`${label} icon`}
      className="w-full rounded-xl object-contain"
    />
    <h3 className="text-white font-bold text-center">{label}</h3>
    <div className="bg-slate-200 text-black rounded-md px-2 text-center">{value}</div>
  </div>
);

FactorCard.propTypes = {
  icon: PropTypes.string.isRequired,
  label: PropTypes.string.isRequired,
  value: PropTypes.string.isRequired,
};

const ServiceCard = ({ cropName, data }) => {
  const navigate = useNavigate();

  const handleGuidNavigate = async () => {
    try {
      const formattedCropName = cropName.trim().toLowerCase();
      console.log('Sending crop name:', formattedCropName); // Debug log
      const response = await axios.post('http://localhost:5000/api/cropDetails', {
        cropName: formattedCropName,
      });
      navigate('/guide', { state: { cropName: cropName, details: response.data } });
      console.log('Received response:', response.data); // Debug log
      
    } catch (error) {
      console.error('Error fetching crop details:', error);
      alert(error.response?.data?.error || 'Crop not found or server error.');
    }
  };

  // Fallback for missing data
  if (!data) {
    return <h3 className="text-red-500">Data not available for the crop: {cropName}</h3>;
  }

  return (
    <Tilt className="w-full">
      <motion.div className="w-full green-pink-gradient p-[4px] rounded-[20px] shadow-card">
        <div
          options={{
            max: 45,
            scale: 1,
            speed: 450,
          }}
          className="bg-[#1a1a1a] rounded-[20px] py-5 px-6 min-h-[280px] flex sm:flex-col flex-col justify-evenly items-center gap-6"
        >
          <div className="grid grid-cols-3 gap-4 w-full place-items-center">
            {/* Each card now checks for the existence of its data */}
            <div className="w-[80px] flex flex-col items-center">
              <img
                src="./atom/temp.jpg"
                alt="Suitable Crop"
                className="w-full rounded-xl object-contain"
              />
              <h3 className="text-white font-bold text-center">Temp</h3>
              <div className="bg-slate-200 text-black rounded-md">
                {data.Temp || 'N/A'}
              </div>
            </div>
            <div className="w-[80px] flex flex-col items-center">
              <img
                src="./atom/rainfall.jpg"
                alt="Suitable Crop"
                className="w-full rounded-xl object-contain"
              />
              <h3 className="text-white font-bold text-center">Rainfall</h3>
              <div className="bg-slate-200 text-black rounded-md">
                {data.Rainfall || 'N/A'}
              </div>
            </div>
            <div className="w-[80px] flex flex-col items-center">
              <img
                src="./atom/ph.jpg"
                alt="Suitable Crop"
                className="w-full rounded-xl object-contain"
              />
              <h3 className="text-white font-bold text-center">pH</h3>
              <div className="bg-slate-200 text-black rounded-md">
                {data.pH || 'N/A'}
              </div>
            </div>
            {/* Additional fields */}
            <div className="w-[80px] flex flex-col items-center">
              <img
                src="./atom/nitrogen.jpg"
                alt="Suitable Crop"
                className="w-full rounded-xl object-contain"
              />
              <h3 className="text-white font-bold text-center">Nitrogen</h3>
              <div className="bg-slate-200 text-black rounded-md">
                {data.Nitrogen || 'N/A'}
              </div>
            </div>
            <div className="w-[80px] flex flex-col items-center">
              <img
                src="./atom/phosphorus.jpg"
                alt="Suitable Crop"
                className="w-full rounded-xl object-contain"
              />
              <h3 className="text-white font-bold text-center">Phosphorus</h3>
              <div className="bg-slate-200 text-black rounded-md">
                {data.Phosphorus || 'N/A'}
              </div>
            </div>
            <div className="w-[80px] flex flex-col items-center">
              <img
                src="./atom/potassium.jpg"
                alt="Suitable Crop"
                className="w-full rounded-xl object-contain"
              />
              <h3 className="text-white font-bold text-center">Potassium</h3>
              <div className="bg-slate-200 text-black rounded-md">
                {data.Potassium || 'N/A'}
              </div>
            </div>
          </div>

          <h4 className="text-white text-center text-[14px] sm:text-[16px]">
            Click here to learn the cultivation method step by step.
          </h4>

          <motion.button
            onClick={handleGuidNavigate}
            whileHover={{ scale: 1.1 }}
            whileTap={{ scale: 0.95 }}
            transition={{ type: 'spring', stiffness: 300 }}
            className="green-pink-gradient text-white px-4 py-2 rounded-md font-medium text-lg shadow-lg hover:bg-blue-600"
          >
            Click
          </motion.button>
        </div>
      </motion.div>
    </Tilt>
  );
};

export default ServiceCard;


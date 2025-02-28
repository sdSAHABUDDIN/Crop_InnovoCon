import React from 'react'
import {motion} from 'framer-motion'
import { fadeIn, textVariant } from '../utils/motion'
import { styles } from '../utils/style'
import {Tilt} from 'react-tilt'
import { useLocation, useNavigate } from 'react-router-dom'
import axios from 'axios'

const ServiceCard = () => {
  const navigation=useNavigate()
  const location=useLocation()
  const {cropName}=location.state || "No crop recommended"
  console.log("crop name is: ",cropName)
  const handleGuidNavigate=async()=>{
    try {
      const response = await axios.post('http://localhost:5000/api/cropDetails', {
        cropName:cropName.trim().toLowerCase(),
      });
      navigation('/guide', { state: { cropName: cropName, details: response.data } });
      
    } catch (error) {
      console.error('Error fetching crop details:', error);
      alert('Crop not found or server error.');
    }  
    
    
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
           // Adjusted parent div height
        >
          {/* Increased image size */}
          <div className='w-full'>
          <img
            src={`./crop/${cropName}.jpg`}
            alt="Suitable Crop"
            className="w-full rounded-xl object-contain" // Increased image size
          />
          </div>
          {/* Decreased text size */}
          <h3 className="text-white text-[18px] sm:text-[22px] font-bold text-center py-1 px-2 rounded-md">
            {cropName} is suitable
          </h3>
          <h4 className="text-white text-center text-[14px] sm:text-[16px]">
          Click here to learn the cultivation method step by step.
          </h4>

          {/* Decreased button size */}
          <motion.button
            whileHover={{ scale: 1.1 }} // Zoom effect on hover
            whileTap={{ scale: 0.95 }} // Slightly shrink on click
            transition={{ type: 'spring', stiffness: 300 }} // Smooth scaling animation
            className="green-pink-gradient text-white px-4 py-2 rounded-md font-medium text-lg shadow-lg hover:bg-blue-600"
            onClick={handleGuidNavigate}
          >
            Click
          </motion.button>
        </div>
      </motion.div>
    </Tilt>
  );
};

const CropPra = () => {
  return (
    <div className="flex flex-col md:flex-row">
      <div >
    <motion.div variants={textVariant()}>
      
      <h2 className={styles.sectionHeadText}>Our Recommendation:</h2>
    </motion.div>
    <motion.p
        variants={fadeIn("", "", 0.1, 1)}
        className='sm:px-16 px-6 mt-4 text-secondary text-[17px] max-w-3xl leading-[30px]'
      >
        Our crop prediction system uses advanced machine learning techniques, specifically a Random Forest Classifier (RFC), to analyze the data you provide. By evaluating key factors such as nitrogen, phosphorus, potassium, temperature, humidity, soil pH, and rainfall, our model predicts the most suitable crop for your conditions.
        <br/>
        This predictive approach is designed to empower farmers and agricultural professionals by providing actionable insights to optimize crop yield and resource efficiency. We aim to support sustainable farming practices, improve decision-making, and ultimately help grow your agricultural business effectively.
      </motion.p>
      </div>
      <div className="sm:px-16 px-6 md:w-1/2 sm:py-16 py-10 flex justify-center">
        <ServiceCard />
      </div>
    </div>
  )
}

export default CropPra
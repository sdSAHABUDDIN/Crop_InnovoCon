import React from 'react'
import {motion} from 'framer-motion'
import {  textVariant } from '../utils/motion'
import { styles } from '../utils/style'

// import Enviropracompo from '../components/Enviropracompo'
import { useLocation } from 'react-router-dom'
import ServiceCard from '../components/ServiceCard'




const EnviroPra = () => {
  const location=useLocation();
  const {cropName,data}=location.state || {};
  console.log("EnviroPra Data:", data);
  if (!data) {
    return <h1 className="text-center text-red-500">No data available for this crop.</h1>;
  }
  console.log(data)
  
  return (
    <div className="flex flex-col ">
      <div  >
    <motion.div variants={textVariant()}>   
      <h2 className={styles.sectionHeadText}>Our Recommendation:</h2>
      <h3 className={styles.sectionSubText}>"We help you identify the optimal environment for your chosen crop by analyzing key factors. Our predictions ensure better growth and yield using advanced data-driven insights."</h3>
      <br></br>
      <h1 className={styles.sectionHeadText}>Crop Name: {cropName}</h1>
    </motion.div>
    
      </div>
      <div className="sm:px-16 px-4 sm:py-5 py-5 flex justify-center">
        <ServiceCard cropName={cropName} data={data[cropName.toLowerCase()]}/>
      </div>
      
    </div>
  )
}

export default EnviroPra
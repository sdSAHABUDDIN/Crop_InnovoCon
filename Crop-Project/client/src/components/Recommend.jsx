import React, { useState } from 'react'
import { motion } from 'framer-motion'


import { sendDataToServer } from '../utils/apiUtils'
import EnviroInputcom from './EnviroInputcom'
import { useNavigate } from 'react-router-dom'

const Recommend = () => {
  const [nitrogen,setNitrogen]=useState("")
  const [phosphorus,setPhosphorus]=useState("")
  const [potassium,setPotassium]=useState("")
  const [temperature,setTemperature]=useState("")
  const [humidity,setHumidity]=useState("")
  const [pH,setpH]=useState("")
  const [rainfall,setRainfall]=useState("")
  const[response,setResponse]=useState(null)
  const navigate=useNavigate()
  
    
 
  const handleChange= async(e)=>{
    e.preventDefault();
    const payload={
      Nitrogen:nitrogen,
      Phosphorus:phosphorus,
      Potassium:potassium,
      Temperature:temperature,
      Humidity:humidity,
      pH:pH,
      Rainfall:rainfall,
    }
    const result= await sendDataToServer("http://localhost:5000/api/predict",payload);
    if(result.success){
      console.log('server response:',result.data);
      const cropName = typeof result.data === "string" ? result.data : result.data.prediction;
      console.log(cropName)
      navigate ('/croppradict',{state:{cropName}})
      
    }else{
      console.log('Error from server:',result.error);
      setResponse({error:result.error})
    }
  }
  
  return (
    <motion.div initial={{opacity:0,y:20}}
    animate={{opacity:1,y:0}}
    transition={{duration:0.5}}
    className='max-w-xl w-full bg-gray-800 bg-opacity-50 backdrop-filter backdrop-blur-xl rounded-2xl shadow-xl overflow-hidden'>
      <div className='p-8'>
        <h2 className='text-3xl font-bold mb-6 text-center bg-gradient-to-r from-green-400 to-emerald-500 text-transparent bg-clip-text'>
        Please provide the recommended value.
        </h2>
        <form onSubmit={handleChange}>
          <span>Nitrogen</span>
          <EnviroInputcom  
          type='Nitrogen'
          placeholder='Enter nitrogen value within 180'
          value={nitrogen}
          onChange={(e) => setNitrogen(e.target.value)
            
          } />
          <span>Phosphorus</span>
           <EnviroInputcom      
          type='Phosphorus'
          placeholder='Enter Phosphorus value within 145'
          value={phosphorus}
          onChange={(e) => setPhosphorus(e.target.value)} />
          <span>Potassium</span>
           <EnviroInputcom
          icon={Lock}
          type='Potassium'
          placeholder='Enter Potassium value within 205'
          value={potassium}
          onChange={(e) => setPotassium(e.target.value)} />
          <span>Temperature</span>
           <EnviroInputcom         
          type='Temperature'
          placeholder='Enter Temperature value within 45'
          value={temperature}
          onChange={(e) => setTemperature(e.target.value)} />
          <span>Humidity</span>
           <EnviroInputcom        
          type='Humidity'
          placeholder='Enter Humidity value within 100'
          value={humidity}
          onChange={(e) => setHumidity(e.target.value)} />
          <span>pH</span>
           <EnviroInputcom         
          type='pH'
          placeholder='Enter pH value within 9'
          value={pH}
          onChange={(e) => setpH(e.target.value)} />
          <span>Rainfall</span>
           <EnviroInputcom          
          type='Rainfall'
          placeholder='Enter Rainfall value within 300'
          value={rainfall} 
          onChange={(e) => setRainfall(e.target.value)}/>
          <motion.button
            
						whileHover={{ scale: 1.05 }}
						whileTap={{ scale: 0.95 }}
						type='submit'
						// disabled={isLoading || code.some((digit) => !digit)}
						className='w-full bg-gradient-to-r from-green-500 to-emerald-600 text-white font-bold py-3 px-4 rounded-lg shadow-lg hover:from-green-600 hover:to-emerald-700 focus:outline-none focus:ring-2 focus:ring-green-500 focus:ring-opacity-50 disabled:opacity-50'
					>
						Submit
					</motion.button>         
        </form>
        {response && (
          <div className='mt-4 text-white'>
            {response.error ? (
              <p className='text-red-500'>{response.error}</p>):(
              <pre>{JSON.stringify(response.data,null,2)}</pre>
            )}</div>
        )}
      </div>
    </motion.div>
  )
}

export default Recommend
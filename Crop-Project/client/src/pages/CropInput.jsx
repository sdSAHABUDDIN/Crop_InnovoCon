import React, { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import axios from 'axios'
import Middlepage from '../components/Middlepage'
const CropInput = () => {
  const[cropName,setCropName]=useState('')
  const navigate=useNavigate();
  const handleSubmit=async(e)=>{
    e.preventDefault();
    if (cropName.trim()){
      try {
        const response = await axios.post('http://localhost:5000/api/enviromentDetails', {
          cropName:cropName.trim().toLowerCase(),
        });
        navigate('/enviropra',{state:{cropName,data:response.data}});
      } catch (error) {
        console.error('Error fetching crop details:', error);
        alert('Crop not found or server error.');
      }    
    }
    else{
      alert('Please enter a crop name')
    }
  }
  return (
    <>
    <div className="relative w-full h-screen bg-cover bg-center"
    style={{ backgroundImage: `url('Agriculture3.jpg')` }}>
      <div className="absolute inset-0 flex flex-col items-center py-10 bg-black bg-opacity-20 text-center ">
        <h1 className="text-white text-3xl sm:text-5xl lg:text-6xl font-bold">
        "Unlock the ideal conditions for your crop to flourish!"
        </h1>
        <p className="text-white text-base sm:text-lg lg:text-xl mt-4 max-w-3xl px-4">
          Discover the most suitable crops for your land using data-driven insights. Empowering sustainable and productive farming.
        </p>
        <div className="absolute inset-0 flex justify-center items-center mt-60">
          <div className="flex flex-col gap-2 justify-center  overflow-x-auto  bg-white bg-opacity-80 rounded-lg shadow-lg text-center  w-[390px] sm:w-[390px] h-[430px]  items-center cursor-pointer">
            <div className="relative bg-cover bg-center w-[350px] h-[150px] rounded-lg"
            style={{ backgroundImage: `url('./crop/Orange.jpg')` }}/>

            
            <div className="relative bg-cover bg-center w-[350px] h-[150px] rounded-lg"
            style={{ backgroundImage: `url('./crop/Cotton.jpg')` }}/>

            
          <form onSubmit={handleSubmit}>
            <input className='pl-10 h-[40px] w-[350px] rounded-lg bg-slate-600  ' type="text" placeholder='Enter your crop name' value={cropName} onChange={(e)=>setCropName(e.target.value)}  />
            <br/>
            <button type='submit' className=' bg-slate-800 mt-2 w-[100px] rounded-lg p-2'>
              Submit
            </button>
          </form>
          </div>
        </div>
      </div>
      
    </div>
    <Middlepage />
    </>
  )
}

export default CropInput
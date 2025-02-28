import React from "react";
import Middlepage from "../components/Middlepage";
import Spline from "@splinetool/react-spline";
import InputSec from "../components/InputSec";
import Train from "../components/Train";
import Feedback from "../components/Feedback";


const Home = () => {
  return (
    <div className="w-full">
      {/* Background 3D Scene */}
      <div className="relative w-full h-screen">
      <Spline scene="https://prod.spline.design/PzQGVCtBbraSnGrR/scene.splinecode" />


        {/* Overlay Section */}
        <div className="absolute inset-0 flex flex-col my-8 bg-opacity-30 text-center">
          <h1 className="text-black text-5xl sm:text-5xl lg:text-6xl font-thin">
            FarmGenius
            <br />
            <i className="font-medium">AI-Based Crop Advisory</i>
          </h1>
        </div>
      </div>

      {/* InputSec Section - Properly Positioned Below Hero Section */}
      <div className="w-full flex justify-center mt-10"> 
        <InputSec />
      </div>
      <div className="w-full flex justify-center mt-10"> 
       <Train />
      </div>
      <div className="w-full flex justify-center mt-10"> 
       <Feedback />
      </div>

      {/* Middlepage Section - Positioned Below InputSec */}
      <div className="w-full mt-10">  
        <Middlepage />
      </div>
    </div>
  );
};

export default Home;

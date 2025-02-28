import React from 'react';
import { motion } from "framer-motion";
import Homecom from "../components/Homecom";
import { useNavigate } from "react-router-dom";

const Card = () => {
  const navigate = useNavigate();

  return (
    <div className="w-full flex justify-center mt-10">
      <div className="flex gap-6 flex-wrap justify-center max-w-full overflow-x-auto px-4">
        {/* Card 1 */}
        <motion.div
          onClick={() => navigate("/cropinput")}
          className="bg-white bg-opacity-80 p-6 rounded-lg shadow-lg w-[250px] sm:w-[300px] h-[420px] text-center flex flex-col items-center cursor-pointer"
        >
          <Homecom />
          <motion.button className="text-lg font-bold text-gray-800 mt-1">
            Click
          </motion.button>
          <p className="text-sm text-gray-600 mt-1">
            Find the right environment for your chosen crop.
          </p>
        </motion.div>

        {/* Card 2 */}
        <motion.div
          onClick={() => navigate("/enviroinput")}
          className="bg-white bg-opacity-80 p-6 rounded-lg shadow-lg w-[250px] sm:w-[300px] h-[420px] text-center flex flex-col items-center cursor-pointer"
        >
          <div
            className="relative bg-cover bg-center w-[240px] h-[150px] rounded-lg"
            style={{ backgroundImage: `url('./crop/Apple.jpg')` }}
          />
          <div
            className="relative bg-cover bg-center w-[240px] h-[150px] rounded-lg mt-2"
            style={{ backgroundImage: `url('./crop/Grapes.jpg')` }}
          />
          <motion.button className="text-lg font-bold text-gray-800 mt-1">
            Click
          </motion.button>
          <p className="text-sm text-gray-600">
            Find the right crop for your environment.
          </p>
        </motion.div>
      </div>
    </div>
  );
};

export default Card;

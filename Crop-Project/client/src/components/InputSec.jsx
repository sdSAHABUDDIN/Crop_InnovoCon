import React from "react";
import { useNavigate } from "react-router-dom";
const InputSec = () => {
  const navigate = useNavigate();
  return (
    <section className="w-full flex justify-center items-center py-10 px-5">
      <div className="flex flex-wrap gap-6 justify-center items-center max-w-6xl">
        {/* Left Content */}
        <div className="text-center max-w-xl flex flex-col items-center">
          <p className="font-semibold text-3xl sm:text-4xl md:text-5xl leading-tight">
            FIND OUR SUSTAINABLE CROP
          </p>
          <h1 className="my-4 text-lg sm:text-xl px-2">
            Simply enter your environment or crop details, and let AI unveil
            the perfect yield and sustainability!
          </h1>
          <img
            className="w-16 sm:w-20 my-3"
            src="https://cdn.prod.website-files.com/63661389dd2417f19a0d89d3/6368b9b6df8f8507ee25ce0f_icon-04.svg"
            loading="lazy"
            alt="AI Icon"
          />
          <p className="my-4 text-sm sm:text-base px-3">
            Through careful analysis, creative thinking, and a deep
            understanding of their goals, we empower businesses to surpass
            expectations and thrive in today's dynamic and competitive
            landscape.
          </p>
          <div className="flex justify-center gap-4 mt-4">
            <button onClick={() => navigate("/card")} className="px-5 py-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600 transition">
              OUR ML MODEL
            </button>
            <button onClick={()=>navigate('/gimini')} className="px-5 py-2 bg-green-500 text-white rounded-lg hover:bg-green-600 transition">
              GEMINI AI
            </button>
          </div>
        </div>

        {/* Right Image Section */}
        <div
          className="w-full sm:w-96 h-56 sm:h-72 md:h-96 bg-cover bg-center rounded-lg"
          style={{ backgroundImage: `url('./1_zd5e.jpg')` }}
        ></div>
      </div>
    </section>
  );
};

export default InputSec;

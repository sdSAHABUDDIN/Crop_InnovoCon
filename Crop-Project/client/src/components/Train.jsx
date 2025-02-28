import React from "react";

const Train = () => {
  return (
    <section className="w-full flex justify-center items-center py-10 px-5">
      <div className="flex flex-col md:flex-row gap-6 justify-between items-center max-w-7xl w-full px-6 md:px-10 lg:px-16">
        {/* Left Content */}
        <div className="w-full md:w-1/2 flex flex-col items-start text-left">
          <p className="font-semibold text-3xl sm:text-4xl md:text-5xl leading-tight">
            CONTACT RENOWNED AGENCIES
          </p>
          <h1 className="my-4 text-lg sm:text-xl">
            Connect with top industry experts and their agencies to accelerate
            the growth of your agricultural business.
          </h1>
          <img
            className="w-16 sm:w-20 my-3"
            src="https://cdn.prod.website-files.com/63661389dd2417f19a0d89d3/6368b9b6df8f8507ee25ce0f_icon-04.svg"
            loading="lazy"
            alt="Agency Icon"
          />
          <h1 className="text-2xl sm:text-3xl my-4">Key Services Offered by Agricultural Agencies:</h1>
          <p className="my-4 text-sm sm:text-base">
            <span className="text-xl">✓</span> Professional Training – Workshops and courses on modern farming techniques, organic farming, and agribusiness strategies.<br />
            <span className="text-xl">✓</span> Technology Integration – Use of AI, IoT, and precision farming tools for better crop yield and resource management.<br />
            <span className="text-xl">✓</span> Market & Business Development – Assistance in connecting farmers with buyers, exporters, and financial institutions.<br />
            <span className="text-xl">✓</span> Government & Funding Support – Helping farmers access government subsidies, loans, and grants for agricultural projects.
          </p>
          <div className="flex justify-start gap-4 mt-4">
            <button className="px-5 py-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600 transition">
              FIND AGENCIES
            </button>
          </div>
        </div>

        {/* Right Image Section */}
        <div
          className="w-full md:w-1/2 h-56 sm:h-72 md:h-96 bg-cover bg-center rounded-lg"
          style={{ backgroundImage: `url('./agency/usa5.jpg')` }}
        ></div>
      </div>
    </section>
  );
};

export default Train;
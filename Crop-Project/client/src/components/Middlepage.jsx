import React, { useState } from 'react';
import { motion } from 'framer-motion';
import { styles } from '../utils/style';

const Middlepage = () => {
  const [isExpanded, setIsExpanded] = useState({
    section1: false,
    section2: false,
    section3: false,
  });

  const toggleReadMore = (section) => {
    setIsExpanded((prev) => ({ ...prev, [section]: !prev[section] }));
  };

  return (
    <motion.div
      className="bg-slate-300 text-black flex flex-col items-center px-4 py-8"
    >
      <div className="container mx-auto grid gap-6 sm:grid-cols-1 md:grid-cols-2 lg:grid-cols-3">
        {/* First Section */}
        <div className={`${styles.padding} shadow-md w-full flex flex-col`}>
          <h1 className="text-xl font-bold mb-2">
            WHY DO WE NEED AGRICULTURE DEVELOPMENT?
          </h1>
          <h4 className="mt-2 text-justify">
            With one-seventh of the world's population, India's economic stability is dependent on the sustained growth of agriculture and allied activities. The Government of India set an ambitious target of doubling farmers' income.
          </h4>
          {isExpanded.section1 && (
            <h4 className="mt-2 text-justify">
              However, the crucial challenge for India's agricultural development is to ensure that small and marginal farmers are able to gain adequate remuneration from farming and contribute to the country's increasing demand for food.
              <br />
              At the same time, cultivable soils are slowly becoming difficult to farm on due to high cropping intensity, inappropriate application of fertilizers, and inadequate usage of manure, among others that are causing severe nutrient deficiencies in soils.
            </h4>
          )}
          <button
            onClick={() => toggleReadMore('section1')}
            className="mt-4 text-blue-500 underline self-start"
          >
            {isExpanded.section1 ? 'Read Less' : 'Read More'}
          </button>
        </div>

        {/* Second Section */}
        <div className={`${styles.padding} shadow-md w-full flex flex-col`}>
          <h1 className="text-xl font-bold mb-2">
            CROP DEMONSTRATIONS
          </h1>
          <h4 className="mt-2 text-justify">
            The Agriculture Development Program uses a learning-by-doing approach to build on the knowledge and capabilities of farmers to maximize their crop productivity and better manage soil health.
          </h4>
          {isExpanded.section2 && (
            <h4 className="mt-2 text-justify">
              The crop demonstrations are carried out on the farmers' own fields, with the control and experimental fields side-by-side. This puts into action the theory of seeing-is-believing, where farmers observe the results themselves.
            </h4>
          )}
          <button
            onClick={() => toggleReadMore('section2')}
            className="mt-4 text-blue-500 underline self-start"
          >
            {isExpanded.section2 ? 'Read Less' : 'Read More'}
          </button>
        </div>

        {/* Third Section */}
        <div className={`${styles.padding} shadow-md w-full flex flex-col`}>
          <h1 className="text-xl font-bold mb-2">
            FARM MECHANIZATION
          </h1>
          <h4 className="mt-2 text-justify">
            Use of appropriate machines and modern technology in agriculture has the potential to address and overcome challenges such as poverty, resource scarcity, climate change, hunger, and malnutrition.
          </h4>
          {isExpanded.section3 && (
            <h4 className="mt-2 text-justify">
              The Agriculture Development Program increases the penetration of mechanization among small and marginal farmers by providing farm machines at subsidized rates, allowing them to earn additional income.
            </h4>
          )}
          <button
            onClick={() => toggleReadMore('section3')}
            className="mt-4 text-blue-500 underline self-start"
          >
            {isExpanded.section3 ? 'Read Less' : 'Read More'}
          </button>
        </div>
      </div>
    </motion.div>
  );
};

export default Middlepage;

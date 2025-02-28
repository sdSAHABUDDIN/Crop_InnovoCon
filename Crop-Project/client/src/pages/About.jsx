import React from 'react'
import { Tilt } from 'react-tilt';
import { motion } from "framer-motion";
import { fadeIn,textVariant } from '../utils/motion';
import { styles } from '../utils/style';
import { services } from '../contant';
const ServiceCard = ({ index, title, icon }) => (
  <Tilt className=' xs:w-[250px] w-full'>
    <motion.div
      variants={fadeIn("right", "spring", index * 0.5, 0.75)}
      className='w-full green-pink-gradient p-[1px] rounded-[20px] shadow-card'
    >
      <div
        options={{
          max: 75,
          scale: 2,
          speed: 500,
        }}
        className='bg-tertiary rounded-[20px] py-5 px-12 min-h-[280px] flex justify-evenly items-center flex-col'
      >
        <img
          src={icon}
          alt='web-development'
          className='w-16 h-16 object-contain'
        />

        <h3 className='text-white text-[20px] font-bold text-center'>
          {title}
        </h3>
      </div>
    </motion.div>
  </Tilt>
);
const About = () => {
  return (
    <>
      <motion.div variants={textVariant()} >
        <p className={`${styles.sectionSubText} mt-2`}>Introduction</p>
        <h2 className={styles.sectionHeadText}>Overview.</h2>
      </motion.div>

      <motion.p
        variants={fadeIn("", "", 0.1, 1)}
        className=' text-black text-[17px] max-w-3xl leading-[30px] sm:px-10 px-6 sm:py-0 py-10'
      >
        I'm a skilled software developer with experience in 
        JavaScript, and expertise in frameworks like React, Node.js, and
        Three.js. I'm a quick learner and collaborate closely with clients to
        create efficient, scalable, and user-friendly solutions that solve
        real-world problems. Let's work together to bring your ideas to life!
      </motion.p>

      <div className='mt-20 flex flex-wrap gap-10 sm:px-16 px-6 sm:py-16 py-10'>
        {services.map((service, index) => (
          <ServiceCard key={service.title} index={index} {...service} />
        ))}
      </div>
    </>
  );
};

export default About
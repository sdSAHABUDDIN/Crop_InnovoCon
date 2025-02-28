import React from 'react';

const Footer = () => {
  return (
    <footer className="w-full  text-black md:justify-between gap-8 sm:px-16 px-6 sm:py-16 py-10  flex c ">
      <div className="flex flex-col items-start  ">
  <h1 className="text-lg font-bold ">COMPANY</h1>
  <div className="w-12 h-1 bg-blue-500 rounded mb-4"></div> {/* Small decorative line */}
  <ul className="space-y-2 mb-2 text-sm ">
    <li>About us</li>
    <li>Our Services</li>
    <li>Privacy Policy</li>
    <li>Affiliate Program</li>
  </ul>
</div>
      <div>
        <h1>GET HELP</h1>
        <div className="w-12 h-1 bg-blue-500 rounded mb-4"></div>
        <ul>
          <li>FAQ</li>
          <li>Documentation</li>
          <li>Elements</li>
          <li>Global</li>
        </ul>
      </div>
      <div>
        <h1>Resources</h1>
        <div className="w-12 h-1 bg-blue-500 rounded mb-4"></div>
        <ul>
          <li>API</li>
          <li>From Validation</li>
          <li>Accessibility</li>
          <li>Community</li>
        </ul>
      </div>
      <div>
        <h1>Follow us</h1>
        <div className="w-12 h-1 bg-blue-500 rounded mb-4"></div>
        <ul>
        <li><a href="#"><i class="fa-brands fa-facebook"></i></a></li>

        <li><a href="#"><i class="fa-brands fa-linkedin"></i></a></li>
        <li><a href="#"><i class="fa-brands fa-instagram"></i></a></li>
      </ul>
      <p className="text-sm">
        © {new Date().getFullYear()} AI-Based Crop Recommendation System. All Rights Reserved.
      </p>
      </div>
      
      
    </footer>
  );
};

export default Footer;
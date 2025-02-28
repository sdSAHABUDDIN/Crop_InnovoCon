import React, { useState } from 'react'
import { Link, useNavigate } from 'react-router-dom'
import { UserPlus, LogIn, LogOut } from "lucide-react";
import {motion} from 'framer-motion'
 
//z-40 transition-all duration-300 
function Navbar() {
  const[open,setOpen]=useState(false)
  const navigate=useNavigate()
  const handleNavigateLogin=()=>{
    navigate('/login')
  }
  return (
        <header className='bg-white fixed z-50 top-0 left-0 w-full  bg-opacity-50 backdrop-blur-md shadow-lg border-b border-emerald-800'>
          <div className='container mx-auto px-4 py-3'>
            <div className='flex flex-wrap justify-between items-center text-black'>
              <Link to="/" >Logo</Link> 
              <div className='md:hidden'>
              {/* Mobile button */}
              <div onClick={()=>setOpen((prev)=>!prev)} className='cursor-pointer'>
                {open?"X":"☰"}
              </div>
              {/* Mobile menu */}
              <div className={` absolute w-full h-screen flex flex-col items-center justify-center gap-4 text-lg font-medium bg-white top-16 transition-all ease-in-out ${open?"-right-0":"-right-[100%]"}`}>
              <Link to="/" className='hover:text-emerald-400 '>Home</Link>
              <Link to="/guidepage" className=''>
                <span className='hover:text-emerald-400 '>Crop Details</span>
              </Link>
              <Link to="/about"> 
              <span className='hover:text-emerald-400 '>About</span>
              </Link>
              
              <motion.button className='bg-gray-700 hover:bg-emerald-400 py-2 px-4 rounded-md flex items-center transition  ease-in-out duration-300'>
              <LogIn className='inline-block mr-1' size={18} />
              <span >Log in</span>
              </motion.button>
              <Link to='signup'>
              <UserPlus className='inline-block mr-1' size={18} />
              <span className='hover:text-emerald-400 '>Sign Up</span></Link>
              {/* <Link>
              <LogOut className='inline-block mr-1' size={18} />
              <span className='hidden sm:inline ml-2'>Log out</span>
              </Link> */}
              </div>
              </div>
              {/* DeskTop menu */}
            <nav className='hidden md:flex flex-wrap items-center gap-2 md:gap-8 text-lg'>
              <Link to="/" className='hover:text-emerald-400 '>Home</Link>
              <Link to="/guidepage">
              
                <span className='hover:text-emerald-400 '>Crop Details</span>
              
              </Link>
              <Link to='/about'>
              
              <span className='hover:text-emerald-400 '>About</span>
              </Link>
              
              <motion.button onClick={handleNavigateLogin} className='bg-green-400 hover:bg-gray-700 py-2 px-4 rounded-md flex items-center transition  ease-in-out duration-300'>
              <LogIn className='inline-block mr-1' size={18} />
              <span >Log in</span>
              </motion.button>
              <Link to='/signup'>
              <UserPlus className='inline-block mr-1' size={18} />
              <span className='hover:text-emerald-400'>Sign Up</span></Link>
              {/* <Link>
              {/* <LogOut className='inline-block mr-1' size={18} />
              <span className='hidden sm:inline ml-2'>Log out</span>
              </Link> */} 
            </nav>
          </div>
          </div>
        </header>
      
  )
}

export default Navbar


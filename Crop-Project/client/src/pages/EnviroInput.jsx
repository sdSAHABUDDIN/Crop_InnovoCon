import React from 'react'
import Recommend from '../components/Recommend'
const EnviroInput = () => {
  return (
    <div className=' min-h-screen text-white overflow-hidden'>
      <div className=' relative z-10 max-w-9xl mx-auto px-4 sm:px-6 lg:px-8 py-16'>
      <h1 className='text-center text-5xl sm:text-6xl font-bold text-emerald-400 mb-4'>
      Explore which crops are suitable for your environment
				</h1>
        <div className='flex justify-center py-5'>
          <Recommend />
        </div>
      </div>
    </div>
  )
}

export default EnviroInput
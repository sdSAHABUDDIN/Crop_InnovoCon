import React from 'react'

const EnviroInputcom = ({...props}) => {
  return (
    <div className='relative mb-6'>
      <input 
      {...props}
      className='w-full pl-10 pr-3 py-2 bg-gray-800 bg-opacity-50 rounded-lg border border-gray-700 focus:border-green-500 focus:ring-2 focus:ring-green-500 text-white placeholder-gray-400 transition duration-200'
			 />
    </div>
  )
}

export default EnviroInputcom
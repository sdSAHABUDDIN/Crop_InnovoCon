import React from 'react'
import { Atom } from '../contant'

const Homecom = () => {
  return (
    <div className="relative w-full h-full grid grid-cols-2 gap-3 p-2 place-items-center ">
      {Atom.map((atom)=>(
        <div className="relative bg-cover bg-center w-[90px] h-[90px] rounded-full"
        key={atom.name}
        style={{ backgroundImage: `url(${atom.img})` }}
          ></div>
      ))}
      
    </div>
  )
}

export default Homecom
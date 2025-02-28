import React from 'react'
import { Atom } from '../contant'

const Enviropracompo = () => {
  return (
    <div>
      hello
      {Atom.map((atom)=>{
        <div className='bg-red-600' key={atom.name}>{atom.name}</div>
      })}
      hello
    </div>
  )
}

export default Enviropracompo
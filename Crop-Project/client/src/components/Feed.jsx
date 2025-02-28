import React from 'react'

const Feed = () => {
  return (
    <>
    <div className="bg-zinc-800 p-8 border-gray-50 flex w-full flex-col gap-4 rounded-lg">
              <div className=" border-gray-500 flex items-center p-2 w-16">
                <div className="img">
                  {/* <img src="" alt=""> */}
                </div>
              </div>
              <div className="Do-content">
                <p className="font-normal text-3xl">Amazing Results with Arik's Premium Web Design Services.</p>
              </div>
              <div className="flex items-center p-4 gap-6">
                <p>Arik is a top-notch web designer who created a stunning website for my business. He was attentive to my needs and provided excellent customer service throughout the entire process. I highly recommend his services.</p>
              </div>
              <div className="man">
                <div className="img-man">
                  {/* <img src="./man.png" alt=""> */}
                </div>
                <div className="font-light text-2xl">
                  <p className="name">MATTHEW SMITH</p>
                  <p className="font-normal text-gray-600">Sonic</p>
                </div>
              </div>
            </div>
    </>
  )
}

export default Feed
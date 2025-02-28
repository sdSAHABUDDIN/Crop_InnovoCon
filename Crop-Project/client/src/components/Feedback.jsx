import React from 'react'
import Feed from './Feed'

const Feedback = () => {
  return (
    <div className="w-full text-white p-9">
      <div  className="flex w-full flex-col gap-3 ">
          <div className="flex flex-col justify-center items-center gap-1 text-black">
            <p className="font-light text-4xl text-center ">What my <br/>
            <i>clients say</i></p>
            <p className="font-light text-2xl text-center">See what my clients have to say about working with me and<br/>the results i helped them achieve.</p>
          </div>
          <div className="flex flex-col md:flex-row gap-[40px] my-3">
            <Feed />
            <Feed />
            <Feed />
          </div>
      </div>
    </div>
  )
}

export default Feedback

/*
 <div class="process-1">
        <div class="padding-div-1">

          <div class="upper-content-1">
            <p class="what">What my <br/>
            <i>clients say</i></p>
            <p class="see">See what my clients have to say about working with me and<br/>the results i helped them achieve.</p>
          </div>

          <div class="all-container">
            <div class="container">
              <div class="hours">
                <div class="img"><img src="" alt=""></div>
              </div>
              <div class="Do-content">
                <p class="amazing">Amazing Results with Arik's Premium Web Design Services.</p>
              </div>
              <div class="arik">
                <p>Arik is a top-notch web designer who created a stunning website for my business. He was attentive to my needs and provided excellent customer service throughout the entire process. I highly recommend his services.</p>
              </div>
              <div class="man">
                <div class="img-man">
                  <img src="./man.png" alt="">
                </div>
                <div class="name-box">
                  <p class="name">MATTHEW SMITH</p>
                  <p class="company">Sonic</p>
                </div>
              </div>
            </div>
            <div class="container">
              <div class="hours">
                <div class="img"><img src="" alt=""></div>
              </div>
              <div class="Do-content">
                <p class="amazing">Amazing Results with Arik's Premium Web Design Services.</p>
              </div>
              <div class="arik">
                <p>Arik is a top-notch web designer who created a stunning website for my business. He was attentive to my needs and provided excellent customer service throughout the entire process. I highly recommend his services.</p>
              </div>
              <div class="man">
                <div class="img-man">
                  <img src="./man.png" alt="">
                </div>
                <div class="name-box">
                  <p class="name">MATTHEW SMITH</p>
                  <p class="company">Sonic</p>
                </div>
              </div>
            </div>
            <div class="container">
              <div class="hours">
                <div class="img"><img src="" alt=""></div>
              </div>
              <div class="Do-content">
                <p class="amazing">Amazing Results with Arik's Premium Web Design Services.</p>
              </div>
              <div class="arik">
                <p>Arik is a top-notch web designer who created a stunning website for my business. He was attentive to my needs and provided excellent customer service throughout the entire process. I highly recommend his services.</p>
              </div>
              <div class="man">
                <div class="img-man">
                  <img src="./man.png" alt="">
                </div>
                <div class="name-box">
                  <p class="name">MATTHEW SMITH</p>
                  <p class="company">Sonic</p>
                </div>
              </div>
            </div>
        </div>
    </div> */
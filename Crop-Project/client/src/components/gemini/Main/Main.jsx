import React, { useContext } from "react";

import { assets } from "../../../assets/assets";
import { Context } from "../../../context/Context";

const Main = () => {
  const {
    onSent,
    recentPrompt,
    showResult,
    loading,
    resultData,
    setInput,
    input,
  } = useContext(Context);

  return (
    <div className="flex-1 min-h-screen bg-black pb-[15vh] relative">
      {/* Navbar */}
      <div className="flex items-center justify-between text-gray-400 text-xl px-5 py-4">
        <p>AI.FARMER</p>
        <img src={assets.user_icon} alt="User" className="w-10 rounded-full" />
      </div>

      <div className="max-w-3xl mx-auto px-4">
        {!showResult ? (
          <>
            {/* Greeting */}
            <div className="mt-12 text-5xl text-gray-300 font-medium px-4">
              <p>
                <span className="bg-gradient-to-r from-blue-500 to-red-500 bg-clip-text text-transparent">
                  Hello, Dev.
                </span>
              </p>
              <p>How can I help you today?</p>
            </div>

            {/* Cards */}
            <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4 mt-10 px-4">
              {[
                {
                  text: "Suggest beautiful places to see on an upcoming road trip",
                  icon: assets.compass_icon,
                },
                {
                  text: "Briefly summarize this concept: urban planning",
                  icon: assets.bulb_icon,
                },
                {
                  text: "Brainstorm team bonding activities for our work retreat",
                  icon: assets.message_icon,
                },
                {
                  text: "Suggest beautiful places to see on an upcoming road trip",
                  icon: assets.code_icon,
                },
              ].map((item, index) => (
                <div
                  key={index}
                  className="bg-[#f0f4f9] p-4 h-48 rounded-lg relative cursor-pointer hover:bg-gray-300 transition"
                >
                  <p className="text-gray-600 text-lg">{item.text}</p>
                  <img
                    src={item.icon}
                    alt="Icon"
                    className="w-9 p-1 rounded-lg absolute bottom-3 right-3"
                  />
                </div>
              ))}
            </div>
          </>
        ) : (
          <div className="p-5 max-h-[70vh] overflow-y-scroll scrollbar-hide">
            {/* User Prompt */}
            <div className="flex items-center gap-4 text-white my-6">
              <img
                src={assets.user_icon}
                alt="User"
                className="w-10 rounded-full"
              />
              <p>{recentPrompt}</p>
            </div>

            {/* AI Response */}
            <div className="flex gap-4 text-white">
              <img
                src={assets.gemini_icon}
                alt="AI"
                className="w-10 rounded-full"
              />
              {loading ? (
                <div className="space-y-2">
                  <div className="h-4 bg-gradient-to-r from-blue-300 via-white to-blue-300 rounded-full animate-pulse"></div>
                  <div className="h-4 bg-gradient-to-r from-blue-300 via-white to-blue-300 rounded-full animate-pulse w-4/5"></div>
                  <div className="h-4 bg-gradient-to-r from-blue-300 via-white to-blue-300 rounded-full animate-pulse w-3/5"></div>
                </div>
              ) : (
                <p
                  className="text-lg leading-7 font-light"
                  dangerouslySetInnerHTML={{ __html: resultData }}
                ></p>
              )}
            </div>
          </div>
        )}

        {/* Search Box */}
        <div className="absolute bottom-0 w-full max-w-3xl mx-auto px-4">
          <div className="flex items-center gap-4 bg-[#f0f4f9] p-3 rounded-full">
            <input
              type="text"
              placeholder="Enter a prompt here"
              value={input}
              onChange={(e) => setInput(e.target.value)}
              className="flex-1 bg-transparent outline-none text-lg p-2"
            />
            <div className="flex gap-3">
              <img
                src={assets.gallery_icon}
                alt="Gallery"
                className="w-6 cursor-pointer"
              />
              <img
                src={assets.mic_icon}
                alt="Mic"
                className="w-6 cursor-pointer"
              />
              {input && (
                <img
                  src={assets.send_icon}
                  alt="Send"
                  className="w-6 cursor-pointer"
                  onClick={onSent}
                />
              )}
            </div>
          </div>

          {/* Disclaimer */}
          <p className="text-center text-sm text-gray-500 mt-2">
            AI.FARMER may display inaccurate info, including about people, so
            double-check its result.
          </p>
        </div>
      </div>
      <div className="h-full bg-black pb-[15vh] relative">
        {/* Navbar */}
        <div className="flex items-center justify-between text-gray-400 text-xl px-5 py-4">
          <p>AI.FARMER</p>
          <img
            src={assets.user_icon}
            alt="User"
            className="w-10 rounded-full"
          />
        </div>

        <div className="max-w-3xl mx-auto px-4">
          {!showResult ? (
            <>
              {/* Greeting */}
              <div className="mt-8 text-4xl text-gray-300 font-medium px-4">
                <p>
                  <span className="bg-gradient-to-r from-blue-500 to-red-500 bg-clip-text text-transparent">
                    Hello, Dev.
                  </span>
                </p>
                <p>How can I help you today?</p>
              </div>

              {/* Cards */}
              <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-2 gap-4 mt-8 px-4">
                {[
                  {
                    text: "Suggest beautiful places to see on an upcoming road trip",
                    icon: assets.compass_icon,
                  },
                  {
                    text: "Briefly summarize this concept: urban planning",
                    icon: assets.bulb_icon,
                  },
                  {
                    text: "Brainstorm team bonding activities for our work retreat",
                    icon: assets.message_icon,
                  },
                  {
                    text: "Suggest beautiful places to see on an upcoming road trip",
                    icon: assets.code_icon,
                  },
                ].map((item, index) => (
                  <div
                    key={index}
                    className="bg-[#f0f4f9] p-4 h-40 rounded-lg relative cursor-pointer hover:bg-gray-300 transition"
                  >
                    <p className="text-gray-600 text-lg">{item.text}</p>
                    <img
                      src={item.icon}
                      alt="Icon"
                      className="w-8 p-1 rounded-lg absolute bottom-3 right-3"
                    />
                  </div>
                ))}
              </div>
            </>
          ) : (
            <div className="p-5 max-h-[60vh] sm:max-h-[70vh] overflow-y-auto scrollbar-hide">
              {/* User Prompt */}
              <div className="flex items-center gap-4 text-white my-6">
                <img
                  src={assets.user_icon}
                  alt="User"
                  className="w-10 rounded-full"
                />
                <p>{recentPrompt}</p>
              </div>

              {/* AI Response */}
              <div className="flex gap-4 text-white">
                <img
                  src={assets.gemini_icon}
                  alt="AI"
                  className="w-10 rounded-full"
                />
                {loading ? (
                  <div className="space-y-2">
                    <div className="h-4 bg-gradient-to-r from-blue-300 via-white to-blue-300 rounded-full animate-pulse"></div>
                    <div className="h-4 bg-gradient-to-r from-blue-300 via-white to-blue-300 rounded-full animate-pulse w-4/5"></div>
                    <div className="h-4 bg-gradient-to-r from-blue-300 via-white to-blue-300 rounded-full animate-pulse w-3/5"></div>
                  </div>
                ) : (
                  <p
                    className="text-lg leading-7 font-light"
                    dangerouslySetInnerHTML={{ __html: resultData }}
                  ></p>
                )}
              </div>
            </div>
          )}

          {/* Search Box */}
          <div className="fixed bottom-4 w-full max-w-3xl mx-auto px-4">
            <div className="flex items-center gap-4 bg-[#f0f4f9] p-3 rounded-full">
              <input
                type="text"
                placeholder="Enter a prompt here"
                value={input}
                onChange={(e) => setInput(e.target.value)}
                className="flex-1 bg-transparent outline-none text-lg p-2"
              />
              <div className="flex gap-3">
                <img
                  src={assets.gallery_icon}
                  alt="Gallery"
                  className="w-6 cursor-pointer"
                />
                <img
                  src={assets.mic_icon}
                  alt="Mic"
                  className="w-6 cursor-pointer"
                />
                {input && (
                  <img
                    src={assets.send_icon}
                    alt="Send"
                    className="w-6 cursor-pointer"
                    onClick={onSent}
                  />
                )}
              </div>
            </div>
            <p className="text-center text-sm text-gray-500 mt-2">
              AI.FARMER may display inaccurate info, including about people, so
              double-check its result.
            </p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Main;

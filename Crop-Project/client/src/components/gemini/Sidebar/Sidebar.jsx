import React, { useContext, useState } from "react";
import { assets } from "../../../assets/assets";
import { Context } from "../../../context/Context";

const Sidebar = () => {
  const [extended, setExtended] = useState(false);
  const { onSent, prevPrompts, setRecentPrompt, newChat } = useContext(Context);

  const loadPrompt = async (prompt) => {
    setRecentPrompt(prompt);
    await onSent(prompt);
  };

  return (
    <div className="hidden sm:flex flex-col justify-between bg-[#f0f4f9] min-h-screen w-[200px] p-6">
      {/* Top Section */}
      <div>
        {/* Menu Button */}
        <img
          onClick={() => setExtended((prev) => !prev)}
          className="w-5 cursor-pointer mb-6"
          src={assets.menu_icon}
          alt="Menu"
        />

        {/* New Chat */}
        <div
          onClick={() => newChat()}
          className="flex items-center gap-2 px-4 py-2 bg-[#e6eaf1] rounded-full text-gray-600 cursor-pointer hover:bg-gray-200 transition"
        >
          <img src={assets.plus_icon} alt="New Chat" className="w-5" />
          {extended && <p className="text-sm">New Chat</p>}
        </div>

        {/* Recent Chats */}
        {extended && (
          <div className="mt-6">
            <p className="text-gray-600 font-semibold">Recent</p>
            {prevPrompts.map((item, index) => (
              <div
                key={index}
                onClick={() => loadPrompt(item)}
                className="flex items-center gap-2 px-4 py-2 mt-2 text-gray-800 cursor-pointer rounded-full hover:bg-gray-200 transition"
              >
                <img src={assets.message_icon} alt="Message" className="w-5" />
                <p className="text-sm truncate">{item.slice(0, 18)} ...</p>
              </div>
            ))}
          </div>
        )}
      </div>

      {/* Bottom Section */}
      <div className="flex flex-col gap-3">
        {/* Help */}
        <div className="flex items-center gap-2 px-4 py-2 cursor-pointer text-gray-800 rounded-full hover:bg-gray-200 transition">
          <img src={assets.question_icon} alt="Help" className="w-5" />
          {extended && <p className="text-sm">Help</p>}
        </div>

        {/* Activity */}
        <div className="flex items-center gap-2 px-4 py-2 cursor-pointer text-gray-800 rounded-full hover:bg-gray-200 transition">
          <img src={assets.history_icon} alt="Activity" className="w-5" />
          {extended && <p className="text-sm">Activity</p>}
        </div>

        {/* Settings */}
        <div className="flex items-center gap-2 px-4 py-2 cursor-pointer text-gray-800 rounded-full hover:bg-gray-200 transition">
          <img src={assets.setting_icon} alt="Settings" className="w-5" />
          {extended && <p className="text-sm">Settings</p>}
        </div>
      </div>
    </div>
  );
};

export default Sidebar;

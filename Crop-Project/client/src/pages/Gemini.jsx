import React, { useState, useContext, useEffect } from "react";

import Sidebar from "../components/gemini/Sidebar/Sidebar";
import Main from "../components/gemini/Main/Main";
import UserModal from "./UserModal";
import { Context } from "../context/Context";

const Gemini = () => {
  const [userDetails, setUserDetails] = useState(null);
  const { onSent } = useContext(Context); // Get onSent from context
  console.log("setUserDetails function in Gemini:", setUserDetails);
  useEffect(() => {
    if (userDetails) {
      // Send first prompt when user details are set
      onSent(userDetails.prompt);
    }
  }, [userDetails]); // Runs when userDetails updates

  return (
    <>
      {/* Show modal if userDetails is not set */}

      {!userDetails && <UserModal onSubmit={setUserDetails} />}

      {/* Show Main UI if userDetails are available */}
      {userDetails && (
        <>
          <div className="flex h-screen">
            {/* Sidebar */}
            <Sidebar />

            {/* Main Content */}
            <div className="flex-1 overflow-hidden">
              <Main />
            </div>
          </div>
        </>
      )}
    </>
  );
};

export default Gemini;

import { createContext, useState, useEffect } from "react";
import run from "../config/gemini";

export const Context = createContext();

const ContextProvider = (props) => {
  const [input, setInput] = useState("");
  const [recentPrompt, setRecentPrompt] = useState("");
  const [prevPrompts, setPrevPrompts] = useState([]);
  const [showResult, setShowResult] = useState(false);
  const [loading, setLoading] = useState(false);
  const [resultData, setResultData] = useState("");

  const delayPara = (index, nextWord) => {
    setTimeout(() => {
      setResultData((prev) => prev + nextWord);
    }, 75 * index);
  };

  const newChat = () => {
    setLoading(false);
    setShowResult(false);
  };

  const onSent = async (prompt) => {
    setResultData("");
    setLoading(true);
    setShowResult(true);

    let response;
    if (prompt !== undefined) {
      response = await run(prompt);
      setRecentPrompt(prompt);
    } else {
      setPrevPrompts((prev) => [...prev, input]);
      setRecentPrompt(input);
      response = await run(input);
    }

    // Format response properly
    let formattedResponse = response
      .replace(/\*\*(.*?)\*\*/g, "<b>$1</b>") // Convert **bold** to <b>bold</b>
      .replace(/\*/g, "")                     // Remove stray asterisks
      .replace(/\n/g, "<br/>");                // Preserve line breaks

    let responseArray = formattedResponse.split(" ");
    
    for (let i = 0; i < responseArray.length; i++) {
      const nextWord = responseArray[i];
      delayPara(i, nextWord + " ");
    }

    setLoading(false);
    setInput("");
  };

  // Run only once when the component mounts
  // useEffect(() => {
  //   onSent("What is React JS? Provide a short note.");
  // }, []);

  const contextValue = {
    prevPrompts,
    setPrevPrompts,
    onSent,
    setRecentPrompt,
    recentPrompt,
    showResult,
    loading,
    resultData,
    input,
    setInput,
    newChat,
  };

  return <Context.Provider value={contextValue}>{props.children}</Context.Provider>;
};

export default ContextProvider;

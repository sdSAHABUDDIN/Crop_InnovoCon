import axios from 'axios'
export const sendDataToServer=async(endpoint,payload)=>{
  try {
    const response= await axios.post(endpoint,payload);
    return {success:true,data:response.data};
  } catch (error) {
    const errorMessage=error.response?error.response.data.error || "server error" : "Network error";
    return {success:false,error:errorMessage};
  }
};
export const sendDataToPradict=async(endpoint,payload)=>{
  try {
    const response= await axios.post(endpoint,payload);
    return {success:true,data:response.data};
  } catch (error) {
    const errorMessage=error.response?error.response.data.error || "server error" : "Network error";
    return {success:false,error:errorMessage};
  }
};
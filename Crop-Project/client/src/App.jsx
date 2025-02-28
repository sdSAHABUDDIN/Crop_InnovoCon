import { Route, Routes } from 'react-router-dom';

import Navbar from './components/Navbar';
 // Import your Footer component
import Home from './pages/Home';
import Default from './pages/Default';
import CropPra from './pages/CropPra';
import EnviroInput from './pages/EnviroInput';
import CropInput from './pages/CropInput';
import EnviroPra from './pages/EnviroPra';
import Guide from './pages/Guide';
import Footer from './components/Footer';
import LoginPage from './pages/Login';

import Guidepage from './pages/Guidepage';
import SignUpPage from './pages/Signup';
import About from './pages/About';
import Card from './components/Card';
import UserModal from './pages/UserModal';
import Gemini from './pages/Gemini';

const App = () => {
  return (
    <div className="min-h-screen  relative overflow-hidden">
      {/* Background overlay */}
      <div className="absolute inset-0 overflow-hidden ">
        <div className="absolute inset-0">
          <div className="absolute top-0 left-1/2 -translate-x-1/2 w-full h-full " />
        </div>
      </div>

      {/* Main content */}
      <div className="relative z-50 pt-10">
        <Navbar />
        <Routes>
          <Route path="/default" element={<Default />} />
          <Route path="/" element={<Home />} />
          <Route path="/croppradict" element={<CropPra />} />
          <Route path='gimini' element={<Gemini />}/>
          <Route path='/card' element={<Card />}/>
          <Route path="/cropinput" element={<CropInput />} />
          <Route path='/usermodal' element={<UserModal/>}/>
          <Route path="/enviroinput" element={<EnviroInput />} />
          <Route path="/enviropra" element={<EnviroPra />} />
          <Route path="/guide" element={<Guide />} />
          <Route path="/guidepage" element={<Guidepage />} />
          <Route path="/login" element={<LoginPage />} />
          <Route path="/signup" element={<SignUpPage />} />
          <Route path="/about" element={<About/>} />
        </Routes>
      </div>

      {/* Footer */}
      <Footer />
    </div>
  );
};

export default App;

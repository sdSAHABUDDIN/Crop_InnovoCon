import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.jsx'
import { BrowserRouter } from 'react-router-dom'
// import App2 from './App2.jsx'

import ContextProvider from './context/Context.jsx'
createRoot(document.getElementById('root')).render(
  <StrictMode>
    <BrowserRouter>
    <ContextProvider>
    <App />
  </ContextProvider>
    </BrowserRouter>
  </StrictMode>,
)

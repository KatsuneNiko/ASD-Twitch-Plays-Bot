<<<<<<< HEAD
import "./App.css";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Sidebar from "./components/Sidebar";
import { Home, Introduction, Help} from "./pages/Home";
import AccountSetting from "./pages/AccountSetting";
import Marcos from "./pages/Marcos"; 
import Participation from "./pages/Participation";
import Statistics from "./pages/Statistics";  
import MouseMacro from "./pages/MouseMacro";


function App() {

  return (
    
    <Router>
      <Sidebar />
      <Routes>
        <Route path='/Home' element={<Home/>} />
        <Route path='/Introduction' element={<Introduction/>} />
        <Route path='/Help' element={<Help/>} />
        <Route path='/Marcos' element={<Marcos/>} />
        <Route path='/Participation' element={<Participation/>} />
        <Route path='/Statistics' element={<Statistics/>} />
        <Route path='/AccountSetting' element={<AccountSetting/>} />
        <Route path="/MouseMacro" element={<MouseMacro />} />
      </Routes>
    </Router>
  );
  }
   
export default App;
=======
import logo from './logo.svg';
import './App.css';
import { Login } from "./Login";
import { Discord } from "./Discord";
import { useState } from 'react';

function App() {

  const [currentForm, setCurrentForm] = useState('login');

  const toggleForm = (formName) => {
    setCurrentForm(formName);
  }


  return (
    <div className="App"> 
    {
      currentForm === "login" ? <Login onFormSwitch={toggleForm}/> : <Discord onFormSwitch={toggleForm} />
    }
     

    </div>
  );
}

export default App;
>>>>>>> c46874a2dce852b7500489dc6844aca991bfaf18

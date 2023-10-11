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
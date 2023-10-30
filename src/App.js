import "./App.css";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Sidebar from "./components/Sidebar";
import { Home, Introduction, Help} from "./pages/Home";
import ChatbotOnDiscord from "./pages/ChatbotOnDiscord";
import CRUDKeyboard from "./pages/CRUDKeyboard";
import CRUDMouse from "./pages/CRUDMouse";
import Statistics from "./pages/Statistics";
import SelectProfile from "./pages/SelectProfile";
import StyleOfPlay from "./pages/StyleOfPlay";
import SplitMode from "./pages/SplitMode";
import ValidKeyword from "./pages/ValidKeyword";

function App() {

  return (
    
    <Router>
      <Sidebar />
      <Routes>
        <Route path='/' element={<Home/>} />
        <Route path='/Introduction' element={<Introduction/>} />
        <Route path='/Help' element={<Help/>} />
        <Route path='/CRUDKeyboard' element={<CRUDKeyboard/>} />
        <Route path='/CRUDMouse' element={<CRUDMouse/>} />
        <Route path='/Statistics' element={<Statistics/>} />
        <Route path='/SelectProfile' element={<SelectProfile/>} />
        <Route path='/StyleOfPlay' element={<StyleOfPlay/>} />
        <Route path='/ChatbotOnDiscord' element={<ChatbotOnDiscord/>} />
        <Route path='/SplitMode' element={<SplitMode/>} />
        <Route path='/ValidKeyword' element={<ValidKeyword/>} />
      </Routes>
    </Router>
  );
  }
   
export default App;
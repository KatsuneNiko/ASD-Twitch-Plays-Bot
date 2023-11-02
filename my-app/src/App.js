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

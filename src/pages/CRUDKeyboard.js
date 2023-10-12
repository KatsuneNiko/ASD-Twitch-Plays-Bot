import React from "react";
import { useState } from 'react';


const CRUDKeyboard = () =>  {
    return (
        <div>
            <h1>CRUD Keyboard</h1>
            <text>This page is used to add and delete keywords. {MyForm} </text> <br /> <br />
            <button>Press to either switch between anarchy or democracy</button>
        </div>
    );
};

function MyForm() {
    const [name, setName] = useState("");
  
    const handleSubmit = (event) => {
      event.preventDefault();
      alert(`The name you entered was: ${name}`)
    }
  
    return (
      <form onSubmit={handleSubmit}>
        <label>Enter your name:
          <input 
            type="text" 
            value={name}
            onChange={(e) => setName(e.target.value)}
          />
        </label>
        <input type="submit" />
      </form>
    )
  }

export default CRUDKeyboard;

/*import React, { useState } from "react";
import './App.css';

const Home = () =>  {
    return ( 
        <div> 
          <h1>Home Page</h1> 
          <br /> 
          <ul> 
            <li> 
              <Link to="/">Home</Link> 
            </li> 
            <li> 
              <Link to="/Marcos"></Link> 
            </li> 
            <li>  
              <Link to="/Participation"></Link> 
            </li> 
            <li>  
              <Link to="/Statistics"></Link> 
            </li> 
            <li>  
              <Link to="/AccountSetting"></Link> 
            </li> 
          </ul> 
        </div> 
      ); 
};

export default Home;
*/

import React from "react";
 
export const Home = () => {
  return (
    <div className="home">
      <h1>GeeksforGeeks About us</h1>
    </div>
  );
};
 
export const Introduction = () => {
  return (
    <div className="home">
      <h1>Introduction</h1>
    </div>
  );
};
 
export const Help = () => {
  return (
    <div className="home">
      <h1>Help</h1>
    </div>
  );
};

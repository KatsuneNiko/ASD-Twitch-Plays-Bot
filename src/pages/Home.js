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

import React, { useEffect, useState } from "react";
 
export const Home = () => {
  const [twitchActive, setTwitchActive] = useState(false);

  useEffect(() => {
    (async () => {
      const request = await fetch('/TwitchConnect');
      const requestJson = await request.json();
      setTwitchActive(requestJson.active);
    })()
  }, []);

  const handleClick = async () => {
    const request = await fetch('/TwitchConnect', {
      method: 'POST',
      body: JSON.stringify({ active: !twitchActive }),
      headers: {
        'Content-Type': 'application/json'
      }
  });
    const requestJson = await request.json();
    setTwitchActive(requestJson.active);
  }

  return (
    <div className="home">
      <h1>ASD-Twitch-Plays-Bot is{twitchActive ? ' ' : ' not '}active!</h1>
      <button onClick={handleClick}>
        Start/stop program
      </button>
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

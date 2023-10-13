import React, { useState } from "react";
import axios from "axios";

export const Login = (props) => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const [success, setSuccess] = useState("");

  const handleLogin = (e) => { // Add 'e' as a parameter
    e.preventDefault(); // Prevent the default form submission
    console.log('Username:', username);
    console.log('Password:', password);

    if (username && password) {
      // Use Axios here to make a POST request to your server
      axios.post(`http://localhost:3521/login`, { username, password })
      .then(response => {
        console.log("Response from server:", response);
        setSuccess("Login Accepted, transfering to the home page");
        setError("");
      })
        .catch(error => {
          // Handle errors
          setError("Login failed. Please check your credentials.");
          setSuccess(""); 
        });
    } else {
      setError('Both fields are required!');
      setSuccess("");
    }
    //<button type="button" class="button" onClick={() => props.onFormSwitch()}>Sign Up</button>
  };
  

    return (
      <div className="login-form">
       <form onSubmit={handleLogin}>
        <div class="input-container">
        <label for="text"><b>Username&nbsp;&nbsp;&nbsp;</b></label>
        <input class="input" type="text" name="username" onChange={e => setUsername(e.target.value)} ></input>
        </div>
        <div class="input-container">
        <label for="password"><b>Password&nbsp;&nbsp;&nbsp;</b></label>
        <input class="input" type="password" name="password" onChange={e => setPassword(e.target.value)}></input>
        </div>
        <button type="submit" class="button">Login</button>
        <button type="button" class="button" onClick={() => props.onFormSwitch(`discord`)}>Invite Discord Bot!</button>
       </form>
       {error && <p className="error">{error}</p>}
       {success && <p className="success">{success}</p>}
       </div>
    )
};

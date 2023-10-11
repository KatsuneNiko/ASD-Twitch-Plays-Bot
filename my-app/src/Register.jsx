import React, { useState } from "react";
import axios from "axios";

export const Register = (props) => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const [success, setSuccess] = useState("");

  const handleRegister = (e) => {
    e.preventDefault(); // Prevent the default form submission
  
    if (username && password) {
      // Create a data object to send to the server
      const data = {
        username: username,
        password: password,
      };
  
      // Make a POST request to your server for registration
      axios.post("http://localhost:3521/login", data)
        .then(response => {
          // Handle a successful registration
          console.log("Registration successful:", response.data);
          setSuccess("Registration successful!");
          // You can also redirect to the login page or perform other actions here.
        })
        .catch(error => {
          // Handle registration errors
          console.error("Registration failed:", error);
          setError("Registration failed. Please check your input.");
        });
    } else {
      setError('Both fields are required!');
    }
  };

  return (
    <div className="login-form">
      <form onSubmit={handleRegister}>
        <div class="input-container">
          <label for="text"><b>Create Username&nbsp;&nbsp;&nbsp;</b></label>
          <input class="input" type="text" name="username" value={username} onChange={(e) => setUsername(e.target.value)}></input>
        </div>
        <div class="input-container">
          <label for="password"><b>Create Password&nbsp;&nbsp;&nbsp;</b></label>
          <input class="input" type="password" name="password" value={password} onChange={(e) => setPassword(e.target.value)}></input>
        </div>
        <button type="button" class="button" onClick={() => props.onFormSwitch()}>Back to login</button>
        <button type="submit" class="button">Sign Up!</button>
      </form>
      {error && <p className="error">{error}</p>}
    </div>
  );
};

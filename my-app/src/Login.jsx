import React, { useState } from "react";

export const Login = () => {
  const [username, setUser] = useState("");
  const [password, setPass] = useState("");
  const [error, setError] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch("supra-secret-shhhh.txt");
      if (!response.ok) {
        throw new Error("Failed to fetch user data."); //idk why this doesnt work lol
      }

      const userData = await response.text();
      const userLines = userData.split("\n");

      for (const line of userLines) {
        const [fileUsername, filePassword] = line.split(",");
        if (fileUsername === username && filePassword === password) {
          setError("LOGIN SUCCESSFUL!");
          return;
        }
        else {
            setError("Invalid username or password.");
        }
      }
      
    } catch {
        //idk what to write here lol, works without anything as intended
    }
  };

    return (
        <div className="login-form">
       <form onSubmit={handleSubmit}>
        <div class="input-container">
        <label for="text"><b>Username&nbsp;&nbsp;&nbsp;</b></label>
        <input class="input" type="text" value={username} onChange={(e) => setUser(e.target.value)}></input>
        </div>
        <div class="input-container">
        <label for="password"><b>Password&nbsp;&nbsp;&nbsp;</b></label>
        <input class="input" type="password" value={password} onChange={(e) => setPass(e.target.value)}></input>
        </div>
        <button type="submit" class="button">Login</button>
       </form>
       {error && <p className="error">{error}</p>}
       </div>
    )
};

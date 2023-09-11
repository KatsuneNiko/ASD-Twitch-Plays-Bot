import React, { useState } from "react";
export const Login = () => {
    const[username, setUser] = useState('');
    const[password, setPass] = useState('');
    return (
        <div className="login-form">
       <form>
        <div class="input-container">
        <label for="text"><b>Username&nbsp;&nbsp;&nbsp;</b></label>
        <input value={username} class="input" type="text"></input>
        </div>
        <div class="input-container">
        <label for="password"><b>Password&nbsp;&nbsp;&nbsp;</b></label>
        <input value={password} class="input" type="password"></input>
        </div>
        <button type="submit" class="button">Login</button>
       </form>
       </div>
    )
}
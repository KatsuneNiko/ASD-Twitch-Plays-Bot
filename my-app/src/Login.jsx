import React, { useState } from "react";
export const Login = () => {
    const[username, setUser] = useState('');
    const[password, setPass] = useState('');
    return (
       <form>
        <label for="text">Username</label>
        <input value={username} type="text"></input>
        <label for="password">Password</label>
        <input value={pass} type="password"></input>
        <button>Login</button>
       </form>
    )
}
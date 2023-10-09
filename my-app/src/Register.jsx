import React, { useState } from "react";

export const Register = (props) => {
  const [username, setUser] = useState("");
  const [password, setPass] = useState("");
  const [error, setError] = useState("");


return (

<form>
    <button type="register" class="button" onClick={() => props.onFormSwitch('login')}>Login</button>
    </form>
)

};
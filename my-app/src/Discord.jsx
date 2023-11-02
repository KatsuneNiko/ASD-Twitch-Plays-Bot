import React, { useState } from "react";

export const Discord = (props) => {
  const [error, setError] = useState("");
  
  const handleBotAuthorization = () => {
    window.location.href = "https://discord.com/oauth2/authorize?client_id=1161947969969455174&permissions=14081024&redirect_uri=http%3A%2F%2Flocalhost%3A8919%2F&response_type=code&scope=bot%20guilds%20identify%20connections%20messages.read%20guilds.join%20email%20gdm.join";
  };

  return (
    <div className="login-form">
      <form>
        {/* Other form elements */}
        <button type="button" className="button" onClick={() => props.onFormSwitch("login")}>
          Back to login
        </button>
        <button type="button" className="button" onClick={handleBotAuthorization}>
          Add Bot to Server
        </button>
      </form>
      {error && <p className="error">{error}</p>}
    </div>
  );
};

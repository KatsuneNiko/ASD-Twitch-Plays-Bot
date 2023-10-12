import React, { useEffect, useState } from "react"

const StyleOfPlay = () =>  {    
    
    const [SOP, setSOP] = useState([])
    
        fetch('/StyleOfPlay').then(response => {
            return response.json()
          }).then(data => {
            setSOP(data)
            console.log(data);
          })
      

    return (
        <div>
            <h1>Style of Play</h1>
            <text>Style of play is currently set to... {SOP.getSOP} </text> <br /> <br />
            <button >Press to either switch between anarchy or democracy</button>
        </div>
    );
}
    
export default StyleOfPlay;


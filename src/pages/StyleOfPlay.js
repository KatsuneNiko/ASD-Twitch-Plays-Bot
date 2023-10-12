import React, { useEffect, useState } from "react"



const StyleOfPlay = () =>  {
    const [SOP, setSOP] = useState([])

    const fetchAPI = () => {
        fetch('/StyleOfPlay').then(response => {
            return response.json()
          }).then(data => {
            setSOP(data)
            console.log(data);
          })
      }

    useEffect(() => {
        fetchAPI()
      }, [])
    

    return (
        <div>
            <h1>Style of Play</h1>
            <text>Style of play is currently set to... {SOP.getSOP} </text>
        </div>
    );
    
};



export default StyleOfPlay;


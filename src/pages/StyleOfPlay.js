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
      handleSubmit(event) {
        const axios = require('axios');
        const baseUrl = 'http://localhost:5000'
    
        axios.post('http://localhost:5000/api/create', JSON.stringify(params))
            .end((error, response) => {
                if (!error && response) {
                    console.log('got a valid response from the server')
                } else {
                    console.log(`Error fetching data from the server: `, error)
                }
            });
    
        event.preventDefault();
    }
      
    return (
        <div>
            <h1>Style of Play</h1>
            <text>Style of play is currently set to... {SOP.getSOP} </text> <br /> <br />
            <text>Select one of the follow to switch modes... </text> <br />
            <button onClick={() => switchToAnarchy()} >Anarchy mode</button>
            <button onClick={() => switchToDemocracy()}>Democracy mode</button>

        </div>
    );
    
};



export default StyleOfPlay;


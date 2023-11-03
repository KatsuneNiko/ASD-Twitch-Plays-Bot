import React, { useEffect, useState } from "react"
import "./styleNeko.css";

const StyleOfPlay = () =>  {    

    const [SOP, setSOP] = useState([])

    useEffect(() => {
        (async () => {
            const request = await fetch('/StyleOfPlay');
            const requestJson = await request.json();
            setSOP(requestJson.getSOP);
            //console.log(SOP);
        })()
    }, []);
    
    const handleSubmit = async () => {
        const request = await fetch('/StyleOfPlay', {
            method: 'POST',
            body: JSON.stringify({ 
                trigger: 'true',
            }),
            headers: {
                'Content-Type': 'application/json',
            }
        });
        const requestJson = await request.json();
        setSOP(requestJson.getSOP); //one posted, api returns
    }

    return (
        <div class="vertical-align-content">
            <h1>Style of Play</h1> <br />
            <text>Style of play is currently set to: {SOP} </text> <br /> <br />
            <text>Press the button below to switch between democracy and anarchy mode... </text> <br /> <br />
            <button class="rectangle" action="" onClick={() => handleSubmit()}>Press to switch</button>
        </div>
    );
}
    
export default StyleOfPlay;


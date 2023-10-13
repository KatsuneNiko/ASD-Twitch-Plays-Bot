import React, { useEffect, useState } from "react"

const StyleOfPlay = () =>  {    

    const [SOP, setSOP] = useState([])
    const [value, setValue] = useState('');
    
    function handleSubmit() {
        const data = { name: value };
        console.log('submit');
        console.log(value);
        fetch('/StyleOfPlay/Update'.then(response => {
            return response.json()
            }, [SOP]).then(data => {
            setSOP(data);
            console.log(data);
        }, [SOP]), [])
          .then(res => res.json())
          .then(res => console.log(res));
    }

    function handleValue(e) {
        setValue(e.target.value);
      }

    useEffect(() => {
        fetch('/StyleOfPlay').then(response => {
            return response.json()
            }, [SOP]).then(data => {
            setSOP(data);
            console.log(data);
        }, [SOP]);

    })

    return (
        <div>
            <h1>Style of Play</h1>
            <text>Style of play is currently set to: {SOP.getSOP} </text> <br />
            <text>Press the button below to switch between democracy and anarchy mode... </text> <br /> <br />
            <button action="/StyleOfPlay/Update" onSubmit={handleSubmit}>Press to switch</button>
        </div>
    );
}
    
export default StyleOfPlay;


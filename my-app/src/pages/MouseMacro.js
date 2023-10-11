import React from 'react';

function MouseMacro() {
    const createNewFile = async () => {
        try {
            const response = await fetch('http://localhost:5000/create-text-file', { method: 'POST' });
            const data = await response.json();
            console.log(data.message);
        } catch (error) {
            console.error("Error:", error);
        }
    }

    return (
        <div>
            <h1>Mouse Macro Page</h1>
            <button onClick={createNewFile}>Create New Text File</button>
        </div>
    );
}

export default MouseMacro;

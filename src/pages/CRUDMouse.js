import React, { useState } from 'react';

const CRUDMouse = () => {
  const [selectedCommand, setSelectedCommand] = useState('');
  const [value, setValue] = useState('');
  const [xValue, setXValue] = useState('');
  const [yValue, setYValue] = useState('');

  const possibleCommands = [
    'move_up',
    'move_down',
    'move_left',
    'move_right',
    'click_left',
    'click_right',
    'scroll_up',
    'scroll_down',
    'draw_circle',
    'time',
    'click_coordinates',
    'show_commands'
  ];

  const handleCreateTextFile = async () => {
    try {
      const response = await fetch('http://localhost:5000/create-text-file', {
        method: 'POST',
      });
      const data = await response.json();
      console.log(data.message);
    } catch (error) {
      console.error("Error creating text file:", error);
    }
  };

  const handleLoadAllowedCommands = async () => {
    try {
      const response = await fetch('http://localhost:5000/load-allowed-commands', {
        method: 'POST',
      });
      const data = await response.json();
      console.log(data.commands);
    } catch (error) {
      console.error("Error loading allowed commands:", error);
    }
  };

  const handleAddAllowedCommand = async () => {
    try {
      let commandToSend = selectedCommand;
      if (selectedCommand === 'click_coordinates') {
        commandToSend += `/${xValue},${yValue}`;
      } else {
        commandToSend += `/${value}`;
      }
      const response = await fetch(`http://localhost:5000/add_allowed_command/${commandToSend}`, {
        method: 'POST',
      });
      const data = await response.json();
      console.log(data.message);
    } catch (error) {
      console.error("Error adding allowed command:", error);
    }
  };

  return (
    <div>
      <h1>CRUD Mouse</h1>
      <button onClick={handleCreateTextFile}>Create Text File</button>
      <button onClick={handleLoadAllowedCommands}>Load Allowed Commands</button>
      <div>
        <select value={selectedCommand} onChange={(e) => setSelectedCommand(e.target.value)}>
          {possibleCommands.map((command) => (
            <option key={command} value={command}>
              {command}
            </option>
          ))}
        </select>
        {selectedCommand !== 'click_coordinates' && (
          <input
            type="text"
            placeholder="Value"
            value={value}
            onChange={(e) => setValue(e.target.value)}
          />
        )}
        {selectedCommand === 'click_coordinates' && (
          <>
            <input
              type="text"
              placeholder="X Value"
              value={xValue}
              onChange={(e) => setXValue(e.target.value)}
            />
            <input
              type="text"
              placeholder="Y Value"
              value={yValue}
              onChange={(e) => setYValue(e.target.value)}
            />
          </>
        )}
        <button onClick={handleAddAllowedCommand}>Add Allowed Command</button>
      </div>
    </div>
  );
};

export default CRUDMouse;

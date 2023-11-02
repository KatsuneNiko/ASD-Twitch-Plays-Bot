import React, { Profiler, useEffect, useState } from "react"
import { ScrollView, View, Text, } from "react-native";
import "./styleNeko.css";

const CRUDKeyboard = () =>  {
  //const [SOP, setSOP] = useState([])
  
  const [profileName, setprofileNamez] = useState([])
  const [txtLines, setTextFile] = useState([])

  useEffect(() => {
      (async () => {
          const request = await fetch('/CRUDKeyboard');
          console.log('test');
          const requestJson = await request.json();
          setTextFile(requestJson.txtArray);
          setprofileNamez(requestJson.profileName);
          console.log("txtArray: " + txtLines);
          console.log("profileNamez: " + profileName);
      })()
  }, []);

  const convertToJSON = (data) => {
    return data.split('\n\n').map(entry => {
      return JSON.parse(entry);
    });
  }

  const txtArray = txtLines.toString().split(',');
  const anotherArray = txtLines.toString().split('\n').join("\n\n")
  //txtLines
  //const txtFile = "backend/profiles/" + txtLines
  //const txtList = txtFile.split("/")
  //console.log("List " + txtList);
  
  const handleSubmit = async () => {
    const request = await fetch('/CRUDKeyboard', {
        method: 'POST',
        body: JSON.stringify({ 
          deleteAdd: 'add',
          action: Document.getElementById("press"),
          duration: Document.getElementById("duration"),
          keyword: Document.getElementById("keyword"),
          keybind: Document.getElementById("keybind"),
        }),
        headers: {
          'Content-Type': 'application/json',
          'Accept': 'application/json'
        }
    });
    const requestJson = await request.json();
    console.log(requestJson.txtArray);
    setTextFile(requestJson.txtArray); //one posted, api returns
    
}
  
  return (
    <div class="vertical-align-content">
      <h1>Keywords to Keybind</h1>
        <h2>Profile selected: {profileName}</h2>
        <h2>Existing keywords</h2>
          <text>Format: action, duration, keyword, keybind</text> <br />
      <div class ="scrollable"> {txtLines} </div>
      <div class="row">
        <div class="column">
          <h2>Add keyword</h2>
          <form id="addForm" name="addForm" method="post">
              <p>Action</p>
                <input type = "radio" id="press" value ="press" name="action" required></input>
                <label for="html">Press</label><br></br>
                <input type = "radio" id="hold" value ="hold" name="action" required></input>
                <label for="html">Hold</label><br></br>
              <p>Duration (Seconds)</p>
                <select id="duration" name="duration" required>
                  <option value="1">1</option>
                  <option value="2">2</option>
                  <option value="3">3</option>
                  <option value="5">5</option>
                </select> <br></br>
              <p>Keyword</p> 
                <input type="text" id="keyword" name="keyword" required></input> <br></br>
              <p>Keybind</p> 
                <input type="text" id="keybind" name="keybind" maxLength={1} required></input> <br></br><br></br>
              <button class="rectangle" name="formOneOrTwo" value="add">Add</button> <br></br><br></br>
          </form>
          </div>
          <h2>Delete keyword</h2>
          <div class="column">
            <form id="deleteForm" name="deleteForm" method="post">
                <p>Keyword</p> 
                  <input type="text" id="deleteKeyword" name="deleteKeyword" required></input> <br></br> <br></br>
                <button class="rectangle" id="form2" name="formOneOrTwo" value="delete">Delete</button> 
            </form>
          </div>
      </div>
    </div>
  ); 
};

function MyForm() {
    const [name, setName] = useState("");
  
    const handleSubmit = (event) => {
      event.preventDefault();
      alert(`The name you entered was: ${name}`)
    }
  
    return (
      <form onSubmit={handleSubmit}>
        <label>Enter your name:
          <input 
            type="text" 
            value={name}
            onChange={(e) => setName(e.target.value)}
          />
        </label>
        <input type="submit" />
      </form>
    )
  }

export default CRUDKeyboard;

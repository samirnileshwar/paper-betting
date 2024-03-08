import "./App.css";
import React, { useState, useEffect } from "react";

function App() {
  const url = "http://127.0.0.1:8000/api/events/live/lines/";
  const [data, setData] = useState([]);

  const fetchInfo = () => {
    return fetch(url)
      .then((res) => res.json())
      .then((d) => setData(d))
  }


  useEffect(() => {
    fetchInfo();
  }, []);

  return (
    <div className="App">
      <h1 style={{ color: "green" }}>Paper Betting!</h1>
      <center>
        {data.map((dataObj, index) => {
          return (
            <div
              style={{
                width: "30em",
                backgroundColor: "#35D841",
                padding: 2,
                borderRadius: 10,
                marginBlock: 10,
              }}
            >
              <p style={{ fontSize: 10, color: 'white' }}>{dataObj.away_team} vs {dataObj.home_team}</p>
              {dataObj.line_set.map((line, index) => {
                return (
                  <p style={{ fontSize: 7, color: 'white' }}>{line.line_type}: {line.name} {line.price} {line.point}</p>
                )
              })}
            </div>
          );
        })}
      </center>
    </div>
  );
}

export default App;
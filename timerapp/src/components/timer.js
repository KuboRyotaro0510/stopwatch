import React, { useRef, useState } from "react";

function Stopwatch() {
  const [time, setTime] = useState(0);
  const [isRunning, setIsRunning] = useState(false);
  const intervalRef = useRef(null);
  const [laplist, setLaplist] = useState([]);

  function handleStart() {
    setIsRunning(true);
    intervalRef.current = setInterval(() => {
      setTime((prevTime) => prevTime + 10);
    }, 10);
  }

  function handlePause() {
    clearInterval(intervalRef.current);
    setIsRunning(false);
  }

  function handleReset() {
    clearInterval(intervalRef.current);
    setIsRunning(false);
    setTime(0);
    setLaplist((laplist) => []);
    const list = document.getElementById("list");
    while (list.firstChild) {
      list.removeChild(list.firstChild);
    }
  }

  function handleLap() {
    const milliseconds = `0${(time % 1000) / 10}`.slice(-2);
    const seconds = `0${Math.floor(time / 1000) % 60}`.slice(-2);
    const minutes = `0${Math.floor(time / 60000) % 60}`.slice(-2);
    const hours = `0${Math.floor(time / 3600000)}`.slice(-2);
    const laptime = hours + ":" + minutes + ":" + seconds + ":" + milliseconds;
    setLaplist((currentLaplist) => [...currentLaplist, time]);
    const list = document.getElementById("list");
    let lapHistory = document.createElement("li");
    lapHistory.textContent = laptime;
    list.appendChild(lapHistory);
  }

  const milliseconds = `0${(time % 1000) / 10}`.slice(-2);
  const seconds = `0${Math.floor(time / 1000) % 60}`.slice(-2);
  const minutes = `0${Math.floor(time / 60000) % 60}`.slice(-2);
  const hours = `0${Math.floor(time / 3600000)}`.slice(-2);

  return (
    <>
      <div id="sw">
        <h1>Stopwatch</h1>
        <p>
          {hours}:{minutes}:{seconds}:{milliseconds}
        </p>
        {isRunning ? (
          <button onClick={handlePause}>Pause</button>
        ) : (
          <button onClick={handleStart}>Start</button>
        )}
        <button onClick={handleLap}>lap</button>
        <button onClick={handleReset}>Reset</button>
      </div>
      <ul id="list"></ul>
      <div>
        <link rel="stylesheet" href="" />
      </div>
    </>
  );
}

export default Stopwatch;

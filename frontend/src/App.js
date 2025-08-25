
import React, { useEffect, useState } from "react";
import axios from "axios";
import "./App.css";
const API_URL = process.env.REACT_APP_API_URL;
import Dashboard from "./components/Dashboard";
import BuildList from "./components/BuildList";

function App() {
  const [summary, setSummary] = useState(null);
  const [builds, setBuilds] = useState([]);

  useEffect(() => {
  axios.get(`${API_URL}/metrics/summary`).then((res) => setSummary(res.data));
  axios.get(`${API_URL}/builds/`).then((res) => setBuilds(res.data));
  }, []);

  return (
    <div>
      <h1>CI/CD Health Dashboard</h1>
      <Dashboard summary={summary} />
      <BuildList builds={builds} />
    </div>
  );
}

export default App;

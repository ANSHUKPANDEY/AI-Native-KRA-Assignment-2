import React, { useEffect, useState } from "react";
import axios from "axios";
import Dashboard from "./components/Dashboard";
import BuildList from "./components/BuildList";

function App() {
  const [summary, setSummary] = useState(null);
  const [builds, setBuilds] = useState([]);

  useEffect(() => {
    axios.get("/metrics/summary").then((res) => setSummary(res.data));
    axios.get("/builds").then((res) => setBuilds(res.data));
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

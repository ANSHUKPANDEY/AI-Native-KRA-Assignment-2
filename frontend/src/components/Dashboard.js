
import React from "react";
import "../App.css";

function BarChart({ success, failure }) {
  const total = success + failure;
  const successPercent = total ? (success / total) * 100 : 0;
  const failurePercent = total ? (failure / total) * 100 : 0;
  return (
    <div className="bar-chart">
      <h3>Build Success vs Failure</h3>
      <div style={{ display: "flex", height: "30px", width: "100%", background: "#eee", borderRadius: "6px", overflow: "hidden" }}>
        <div style={{ width: `${successPercent}%`, background: "#4caf50" }}></div>
        <div style={{ width: `${failurePercent}%`, background: "#f44336" }}></div>
      </div>
      <div style={{ display: "flex", justifyContent: "space-between", marginTop: "8px" }}>
        <span style={{ color: "#4caf50" }}>Success: {success}</span>
        <span style={{ color: "#f44336" }}>Failure: {failure}</span>
      </div>
    </div>
  );
}

function Dashboard({ summary }) {
  if (!summary) return <div>Loading metrics...</div>;
  return (
    <div>
      <h2>Pipeline Metrics</h2>
      <div className="dashboard-container">
        <div className="dashboard-card">
          <h3>Total Builds</h3>
          <div className="metric">{summary.total}</div>
        </div>
        <div className="dashboard-card">
          <h3>Success</h3>
          <div className="metric" style={{ color: '#4caf50' }}>{summary.success}</div>
        </div>
        <div className="dashboard-card">
          <h3>Failure</h3>
          <div className="metric" style={{ color: '#f44336' }}>{summary.failure}</div>
        </div>
        <div className="dashboard-card">
          <h3>Avg Build Time</h3>
          <div className="metric">{summary.avg_time}</div>
        </div>
        <div className="dashboard-card">
          <h3>Last Status</h3>
          <div className="metric">{summary.last_status}</div>
        </div>
      </div>
      <BarChart success={summary.success} failure={summary.failure} />
    </div>
  );
}

export default Dashboard;

import React from "react";

function Dashboard({ summary }) {
  if (!summary) return <div>Loading metrics...</div>;
  return (
    <div>
      <h2>Pipeline Metrics</h2>
      <ul>
        <li>Total Builds: {summary.total}</li>
        <li>Success: {summary.success}</li>
        <li>Failure: {summary.failure}</li>
        <li>Average Build Time: {summary.avg_time}</li>
        <li>Last Build Status: {summary.last_status}</li>
      </ul>
    </div>
  );
}

export default Dashboard;

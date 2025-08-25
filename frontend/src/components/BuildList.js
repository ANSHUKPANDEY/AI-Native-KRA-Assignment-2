
import React from "react";
import "../App.css";

const sampleBuilds = [
  { id: 1, pipeline: "GitHub Actions", status: "Success", build_time: 120, timestamp: "2025-08-25 10:00", success: true },
  { id: 2, pipeline: "Jenkins", status: "Failure", build_time: 95, timestamp: "2025-08-25 09:30", success: false },
  { id: 3, pipeline: "GitHub Actions", status: "Success", build_time: 110, timestamp: "2025-08-25 09:00", success: true },
];

function BuildList({ builds }) {
  const displayBuilds = builds.length ? builds : sampleBuilds;
  return (
    <div>
      <h2>Build Executions</h2>
      <table className="build-table">
        <thead>
          <tr>
            <th>ID</th>
            <th>Pipeline</th>
            <th>Status</th>
            <th>Build Time (s)</th>
            <th>Timestamp</th>
            <th>Success</th>
          </tr>
        </thead>
        <tbody>
          {displayBuilds.map((build) => (
            <tr key={build.id}>
              <td>{build.id}</td>
              <td>{build.pipeline}</td>
              <td style={{ color: build.success ? '#4caf50' : '#f44336' }}>{build.status}</td>
              <td>{build.build_time}</td>
              <td>{build.timestamp}</td>
              <td>{build.success ? "Yes" : "No"}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default BuildList;

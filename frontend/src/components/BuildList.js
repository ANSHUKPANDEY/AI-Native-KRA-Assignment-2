import React from "react";

function BuildList({ builds }) {
  if (!builds.length) return <div>No builds found.</div>;
  return (
    <div>
      <h2>Build Executions</h2>
      <table border="1">
        <thead>
          <tr>
            <th>ID</th>
            <th>Pipeline</th>
            <th>Status</th>
            <th>Build Time</th>
            <th>Timestamp</th>
            <th>Success</th>
          </tr>
        </thead>
        <tbody>
          {builds.map((build) => (
            <tr key={build.id}>
              <td>{build.id}</td>
              <td>{build.pipeline}</td>
              <td>{build.status}</td>
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

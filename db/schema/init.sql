-- PostgreSQL schema for CI/CD Health Dashboard
CREATE TABLE builds (
    id SERIAL PRIMARY KEY,
    pipeline VARCHAR(255) NOT NULL,
    status VARCHAR(50) NOT NULL,
    build_time FLOAT NOT NULL,
    timestamp TIMESTAMP NOT NULL,
    logs TEXT,
    success BOOLEAN NOT NULL
);

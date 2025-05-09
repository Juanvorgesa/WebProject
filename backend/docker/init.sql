CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(48) UNIQUE NOT NULL,
    email VARCHAR(64) NOT NULL,
    password VARCHAR(128) NOT NULL
);

CREATE TABLE pumps (
    id SERIAL PRIMARY KEY,
    name VARCHAR(64) NOT NULL,
    ubication VARCHAR(128),
    min_voltage DECIMAL(5,2),
    max_voltage DECIMAL(5,2),
    min_elec_current DECIMAL(5,2),
    max_elec_current DECIMAL(5,2),
    min_flow DECIMAL(6,2),
    max_flow DECIMAL(6,2),
    state BOOLEAN NOT NULL DEFAULT FALSE
);

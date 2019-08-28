CREATE TABLE players (
    id VARCHAR(20),
    win INT DEFAULT 0 NOT NULL,
    loss INT DEFAULT 0 NOT NULL,
    draw INT DEFAULT 0 NOT NULL,
    logged_in INT DEFAULT 0 NOT NULL,
    PRIMARY KEY (id)
);
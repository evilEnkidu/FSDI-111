CREATE TABLE IF NOT EXISTS task (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(64),
        summary VARCHAR(128),
        description TEXT, 
        is_done BOOLEAN DEFAULT 0
);

INSERT INTO task (
        name, 
        summary,
        description
) VALUES (
        "wash car",
        "take the car for a walk",
        "make sure to get more wax"
),
(
        "walk the walk",
        "fido needs his exercise",
        "10 laps around the park should be enough"
),
(
        "buy groceries",
        "get everything on the list",
        "we need tomatoes, potatos"
);
CREATE TABLE IF NOT EXISTS Therapist (
	id UUID UNIQUE DEFAULT uuid_generate_v4(),
	name TEXT NOT NULL,
	username TEXT NOT NULL,
	password VARCHAR(512) NOT NULL,
	PRIMARY KEY(id)
);
SELECT * FROM Therapist;
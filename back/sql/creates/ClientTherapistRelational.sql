CREATE TABLE IF NOT EXISTS ClientTherapistRelational (
	id UUID UNIQUE DEFAULT uuid_generate_v4(),
	therapistID uuid NOT NULL,
	clientID uuid NOT NULL,
	PRIMARY KEY(id),
	FOREIGN KEY(therapistID) REFERENCES Therapist(id),
	FOREIGN KEY(clientID) REFERENCES Client(id)
);
SELECT * FROM ClientTherapistRelational;
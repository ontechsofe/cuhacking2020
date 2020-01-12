CREATE TABLE IF NOT EXISTS InteractionSessionRelational (
	id UUID UNIQUE DEFAULT uuid_generate_v4(),
	interactionID UUID NOT NULL,
	sessionID UUID NOT NULL,
	PRIMARY KEY(id),
	FOREIGN KEY(interactionID) REFERENCES Interaction(id),
	FOREIGN KEY(sessionID) REFERENCES Session(id)
);
SELECT * FROM InteractionSessionRelational;
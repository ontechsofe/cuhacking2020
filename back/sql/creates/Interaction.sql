CREATE TABLE IF NOT EXISTS Interaction (
	id UUID UNIQUE DEFAULT uuid_generate_v4(),
	message TEXT NOT NULL,
	senderID uuid NOT NULL,
	recipientID uuid NOT NULL,
	time BIGINT NOT NULL,
	PRIMARY KEY(id),
	FOREIGN KEY(senderID) REFERENCES Client(id),
	FOREIGN KEY(recipientID) REFERENCES Client(id)
);
SELECT * FROM Interaction;
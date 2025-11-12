CREATE TABLE contact_messages (
    -- A unique ID for each message, making it the primary key.
    message_id INT AUTO_INCREMENT PRIMARY KEY,
    -- Store the sender's name or location (based on the "Your Location" field).
    -- Assuming it might store a name or location text, NVARCHAR is flexible.
    sender_location VARCHAR(255) NOT NULL,
    -- Store the sender's email address.
    sender_email VARCHAR(255) NOT NULL,
    -- Store the actual message text. TEXT is used for potentially long content.
    message_content TEXT NOT NULL,
    -- Records the exact time the message was received.
    submission_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    -- An optional field to track if the message has been reviewed/replied to.
    is_read BOOLEAN DEFAULT FALSE
);

-- Note: In PostgreSQL, you would use 'SERIAL' instead of 'INT AUTO_INCREMENT'
-- and possibly 'VARCHAR(255)' instead of 'NVARCHAR(255)'.
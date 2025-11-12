CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50),
    password VARCHAR(255)
);

CREATE TABLE meetings (
    id INT AUTO_INCREMENT PRIMARY KEY,
    room_id VARCHAR(100),
    host_user_id INT,
    start_time DATETIME,
    end_time DATETIME
);

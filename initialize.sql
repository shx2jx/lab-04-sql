CREATE TABLE users (
user_id INT PRIMARY KEY,
name  VARCHAR(100),
email VARCHAR(254),
created_at DATETIME);

CREATE TABLE posts(
post_id INT PRIMARY KEY,
user_id INT,
post_title VARCHAR(100),
caption TEXT,
created_at DATETIME,
FOREIGN KEY (user_id) REFERENCES users(user_id));

INSERT INTO users VALUES (1, 'Prabhav', 'shx2jx@virginia.edu', '2026-09-01 10:00:00');
INSERT INTO users VALUES (2, 'Saanvi', 'saanvi@email.com', '2026-09-02 11:00:00');
INSERT INTO users VALUES (3, 'Ricky', 'ricky@email.com', '2026-09-03 12:00:00');
INSERT INTO users VALUES (4, 'Ronny', 'ronny@email.com', '2026-09-04 13:00:00');
INSERT INTO users VALUES (5, 'Lucas', 'lucas@email.com', '2026-09-05 14:00:00');
INSERT INTO users VALUES (6, 'Jamie', 'jamie@email.com', '2026-09-06 15:00:00');
INSERT INTO users VALUES (7, 'Morgan', 'morgan@email.com', '2026-09-07 16:00:00');
INSERT INTO users VALUES (8, 'Casey', 'casey@email.com', '2026-09-08 17:00:00');
INSERT INTO users VALUES (9, 'Drew', 'drew@email.com', '2026-09-09 18:00:00');
INSERT INTO users VALUES (10, 'Riley', 'riley@email.com', '2026-09-10 19:00:00');

INSERT INTO posts VALUES (1, 1, 'First Post', 'Hello everyone!', '2026-09-11 10:00:00');
INSERT INTO posts VALUES (2, 2, 'Good Morning', 'Hope everyone has a good day!', '2026-09-12 11:00:00');
INSERT INTO posts VALUES (3, 3, 'Weekend', 'Ready for the weekend.', '2026-09-13 12:00:00');
INSERT INTO posts VALUES (4, 4, 'Food', 'Trying a new restaurant today.', '2026-09-14 13:00:00');
INSERT INTO posts VALUES (5, 5, 'School', 'Another day of classes.', '2026-09-15 14:00:00');
INSERT INTO posts VALUES (6, 1, 'Study Time', 'Studying for my exam.', '2026-09-16 15:00:00');
INSERT INTO posts VALUES (7, 3, 'Game Night', 'Playing games tonight.', '2026-09-17 16:00:00');
INSERT INTO posts VALUES (8, 6, 'Coffee', 'Getting some coffee.', '2026-09-18 17:00:00');
INSERT INTO posts VALUES (9, 8, 'Travel', 'Planning my next trip.', '2026-09-19 18:00:00');
INSERT INTO posts VALUES (10, 10, 'Sunday', 'Relaxing today.', '2026-09-20 19:00:00');
-- I used AI to make the posts section for me as it seemed redundant.  Hope this is ok.

SELECT users.name, posts.post_title, posts.caption
FROM users
JOIN posts ON users.user_id = posts.user_id
WHERE users.name = 'Prabhav';


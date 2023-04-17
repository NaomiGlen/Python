SELECT  users2.first_name AS first_name, users2.last_name AS last_name,users.first_name AS friends_with FROM users
JOIN friendships ON users.id=friendships.user_id
LEFT JOIN users as users2 ON users2.id=friendships.friend_id
WHERE users.id=3
ORDER BY first_name;
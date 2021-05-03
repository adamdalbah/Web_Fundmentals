SELECT users.first_name, users.last_name, user2.first_name as friend_first_name, user2.last_name as friend_last_name FROM users 
JOIN friendships ON users.id = friendships.user_id 
LEFT JOIN users as user2 ON  friendships.friend_id= user2.id
WHERE user.first_name = 'Eli'
ORDER BY user2.first_name




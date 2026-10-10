from insta_utils import likes
from insta_utils import comments

current_likes = 100
new_likes = 25

current_comments = 10
new_comments = 5

updated_likes = likes.like_count(current_likes, new_likes)
updated_comments = comments.comment_count(current_comments, new_comments)

print("Updated Likes:", updated_likes)
print("Updated Comments:", updated_comments)
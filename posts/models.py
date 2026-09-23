from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255)
    text = models.CharField()

# #C-R-U-D
# #create - C

# #INSERT INTO tablename (title, text) VALUES (?, ?)

# #way 1

# post_1 = Post(title="title", text="text")
# post_1.save()

# #way 2
# post_2 = Post.objects.create(title="title2", text="text2")

# #Read - R
# # SELECT * FROM tablename WHERE title IN (asdas)

# posts = Post.objects.filter.all()

# #Update - U
# #UPDATE tablename SET title = title WHERE id = 1;

# post_1.title = "title edited"
# post_1.save()

# #Delete - D
# #DELETE FROM tablename WHERE id = 1;

# post_1.delete()
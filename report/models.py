from django.db import models


class VKUser(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)

    def _is_group(self):
        return self.id < 0

    is_group = property(_is_group)


class Post(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    author = models.ForeignKey(VKUser, on_delete=models.CASCADE, related_name='posts')
    date = models.DateTimeField()
    likes = models.PositiveIntegerField(default=0)


class Comment(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(VKUser, on_delete=models.CASCADE, related_name='comments')
    date = models.DateTimeField()
    likes = models.PositiveIntegerField(default=0)

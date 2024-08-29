from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    #id
    text = models.TextField()
    #related_name добавляет свойство posts к классу User
    #u1 =User()
    #u1.posts тоже самое что Post.objects.filter(author=u1)     !!
    #u1.posts.all() все посты юзера.
    #u1.posts.filter(text='..')
    #если reated_name не указываем . По умолчанию будет post_set
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    favorited_by = models.ManyToManyField(User, related_name="favorites", through='FavoritePost')
    
    #метод определяет как отображаются посты в админке. Не более 50 символов.
    def __str__(self) -> str:
        if len(self.text) > 50:
            return self.text[:47] + '...'
        return f'{self.text[:50]}'

class FavoritePost(models.Model):
    #id
    user = models.ForeignKey(User, on_delete=models.CASCADE , related_name="favorites_lines")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='favorites_lines')
    created_at = models.DateTimeField(auto_now_add=True)

#доступ к свойствам класса Post
#p1 = Post()
#p1.id   #id поста
#p1.text #текст поста
#p1.author.username #доступ к данным в  связанной таблице.


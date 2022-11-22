from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    title = models.TextField(max_length=200, verbose_name='Название группы')
    slug = models.SlugField(unique=True, verbose_name='slug')
    description = models.TextField(verbose_name='Описание группы')

    class Meta:
        verbose_name = 'group'
        verbose_name_plural = 'groups'

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField(verbose_name='Текст поста')
    pub_date = models.DateTimeField(
        verbose_name='Дата публикации',
        auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Автор поста')
    image = models.ImageField(
        upload_to='posts/', null=True, blank=True, verbose_name='Картинка')
    group = models.ForeignKey(
        Group,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='post_group',
        verbose_name='Группа')

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'

    def __str__(self):
        return self.text[:15]


class Comment(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор комментария')
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Пост')
    text = models.TextField(verbose_name='Текст комментария')
    created = models.DateTimeField(
        verbose_name='Дата добавления', auto_now_add=True, db_index=True)

    class Meta:
        verbose_name = 'comment'
        verbose_name_plural = 'comments'

    def __str__(self):
        return self.text[:15]


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower',
        verbose_name='Подписчик')
    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following',
        verbose_name='Автор')

    class Meta:
        verbose_name = 'follow'
        verbose_name_plural = 'follow'

    def __str__(self):
        return self.user

from django.db import models

class Game(models.Model):

    name = models.CharField(max_length=15, verbose_name='название игры')
    description = models.TextField(verbose_name='описание игры')
    stage_num = models.PositiveIntegerField(verbose_name='номер этапа')
    stage_end_date = models.DateField(verbose_name='дата окончания этапа')

    class Meta:

        db_table = 'game'
        verbose_name = 'игра'
        verbose_name_plural = 'игры'

    def __str__(self):
        return f'{self.name}'

class GameUser(models.Model):

    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, verbose_name='имя')
    stage_1 = models.BooleanField(verbose_name='этап 1')
    stage_2 = models.BooleanField(verbose_name='этап 2')
    game = models.ManyToManyField(Game, related_name='game_user', verbose_name='игры')

    class Meta:

        db_table = 'game_user'
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    def __str__(self):
        return f'{self.name}'
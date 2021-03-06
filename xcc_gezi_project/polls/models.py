from django.db import models
from django.utils import timezone
from django.utils.datetime_safe import datetime


# 创建模型类
class Meishi(models.Model):
    id = models.AutoField(primary_key=True)  # 该字段可以不写，它会自动补全
    food_name = models.CharField(max_length=30)  # 设置食物名称
    food_author = models.CharField(max_length=8)  # 设置食物制作人
    food_money = models.FloatField()  # 设置食物价格
    food_star = models.CharField(max_length=10, default='普通')  # 设置食物美味程度

    def __str__(self):  # 重写直接输出类的方法
        return "<Meishi:{id=%s,food_name=%s,food_author=%s,food_money=%s,food_star=%s}>" \
               % (self.id, self.food_name, self.food_author, self.food_money, self.food_star)


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

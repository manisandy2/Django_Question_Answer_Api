from django.db import models

# Create your models here.
from django.db import models


class topic_a(models.Model):
   name = models.CharField(max_length=100)

   def __str__(self):
      return self.name


class topic_b(models.Model):
   name = models.CharField(max_length=100)

   def __str__(self):
      return self.name


class topic_c(models.Model):
   name = models.CharField(max_length=100)

   def __str__(self):
      return self.name


class topic_d(models.Model):
   name = models.CharField(max_length=100)

   def __str__(self):
      return self.name


class Question_1(models.Model):
   ans_1 = models.ForeignKey(topic_a, on_delete=models.DO_NOTHING)
   ans_2 = models.ForeignKey(topic_b, on_delete=models.DO_NOTHING)
   ans_3 = models.ForeignKey(topic_c, on_delete=models.DO_NOTHING)
   ans_4 = models.ForeignKey(topic_d, on_delete=models.DO_NOTHING)
   text_ans = models.TextField(default="",null=True)
from django.db import models

# 学生モデル
class Student(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# 得点モデル
class Score(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='scores')
    subject = models.CharField(max_length=100)
    score = models.IntegerField()

    def __str__(self):
        return f"{self.subject}: {self.score}点"

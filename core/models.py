from django.db import models
from django.conf import settings

class Question(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    @property
    def answers_count(self):
        return self.answer_set.count()

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    body = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    def __str__(self):
        return self.body[:20]
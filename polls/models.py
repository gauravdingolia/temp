from django.db import models


class Question(models.Model):
    QUESTION_TYPE = (('M', 'Multiple Choice'), ('TF', 'True/False'), ('S', 'Subjective'))
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    question_type = models.CharField(max_length=2,choices=QUESTION_TYPE,default='M')

    class Meta:
        app_label = "polls"


    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey('polls.Question', on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    class Meta:
        app_label = 'polls'


    def __str__(self):
        return self.choice_text

from django.db import models

class Ieltsspeakingp1topic(models.Model):
    sp1topic = models.CharField(max_length=1000)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.sp1topic

class Answers(models.Model):
    topic = models.ForeignKey(Ieltsspeakingp1topic, on_delete=models.CASCADE)
    answer = models.TextField()
    uid = models.IntegerField()

    def __str__(self):
        return self.answer

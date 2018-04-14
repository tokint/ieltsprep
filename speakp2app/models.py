from django.db import models

class Ieltsspeakingp2topic(models.Model):
    sp2topic = models.CharField(max_length=1000)
    sp2question = models.CharField(max_length=2000)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.sp2topic

class Answers(models.Model):
    topic = models.ForeignKey(Ieltsspeakingp2topic, on_delete=models.CASCADE)
    answer = models.TextField()
    uid = models.IntegerField()

    def __str__(self):
        return self.answer

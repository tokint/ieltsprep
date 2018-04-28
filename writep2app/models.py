from django.db import models

class Ieltswritingp2topic(models.Model):
    wr2topic = models.CharField(max_length=1000)
    wr2question = models.CharField(max_length=2000)
    wr2sampleurl = models.URLField(max_length=500)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.wr2topic

class Answers(models.Model):
    topic = models.ForeignKey(Ieltswritingp2topic, on_delete=models.CASCADE)
    answer = models.TextField()
    uid = models.IntegerField()

    def __str__(self):
        return self.answer

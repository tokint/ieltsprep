from django.db import models

class Articles(models.Model):
    article_title = models.CharField(max_length=50,default='')
    article_text = models.TextField()
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.article_title

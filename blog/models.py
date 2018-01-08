from django.db import models

class Post(models.Model):
    main = models.CharField(max_length=100)
    body = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.main


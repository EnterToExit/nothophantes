from django.db import models

# Create your models here.


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=64, unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.username

"""class Result(models.Model):
    //user_id = models.ForeignKey(User.user_id)
    submit_time = models.DateTimeField()
    submit_path = models.CharField(max_length=128) // pidorashuesos.mp3
    result_path = models.CharField(max_length=128) // /static/results/012345678-1234-1234-1234-1234"""

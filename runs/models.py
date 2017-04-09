from django.db import models


class Test(models.Model):
    description = models.CharField(max_length=200)

    class Meta:
        db_table = 'test'


class Environment(models.Model):
    description = models.CharField(max_length=200)

    class Meta:
        db_table = 'environment'


class User(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        db_table = 'user'


class Status(models.Model):
    value = models.CharField(max_length=1)

    class Meta:
        db_table = 'status'


class Run(models.Model):
    environment = models.ForeignKey(Environment)
    status = models.ForeignKey(Status)
    user = models.ForeignKey(User)
    test = models.ForeignKey(Test)
    start = models.DateTimeField(null=True)
    end = models.DateTimeField(null=True)

    class Meta:
        db_table = 'run'

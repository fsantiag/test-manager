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
    DEFAULT_STATUSES = (
            ('R', 'Running'),
            ('W', 'Waiting'),
            ('F', 'Failed'),
            ('S', 'Success')
        )
    value = models.CharField(max_length=1, choices=DEFAULT_STATUSES)

    class Meta:
        db_table = 'status'


class Run(models.Model):
    environment = models.ForeignKey(Environment)
    status = models.ForeignKey(Status)
    user = models.ForeignKey(User)
    test = models.ForeignKey(Test)
    start = models.DateField(null=True)
    end = models.DateField(null=True)

    class Meta:
        db_table = 'run'

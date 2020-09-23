from django.db import models

# Create your models here.


class t_url(models.Model):
    name = models.CharField(max_length=50, default='')
    category = models.CharField(max_length=20, default='')
    url = models.CharField(max_length=100, default='')
    order = models.IntegerField()
    status = models.CharField(max_length=20, default='')
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return 't_url {}'.format(self.id)


class t_dict(models.Model):
    name = models.CharField(max_length=50, default='')
    category = models.CharField(max_length=20, default='')
    order = models.IntegerField()
    status = models.CharField(max_length=20, default='')
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return 't_url {}'.format(self.id)


class t_contact(models.Model):
    name = models.CharField(max_length=50, default='')
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    message = models.CharField(max_length=200, default='')
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return 't_url {}'.format(self.id)

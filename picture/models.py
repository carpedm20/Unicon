from django.db import models
from django.core.files import File
from django.core.files.storage import FileSystemStorage

from account.models import Account

upload_to = 'media/picture'

# Create your models here.
def Picture(models.Model):
    title = models.CharField(max_length=100, blank=False)
    slug = models.SlugField(max_length=50, blank=True)

    file = models.FileField(upload_to=upload_to, default = None, blank=True)

    account = models.ForeignKey(Account, blank=True, null=True)
    like_account = models.ManyToManyField(Account, blank=True, null=True)

    tag = models.ManyToManyField('Tag', blank=True, null=True)

    def __unicode__(self):
        return self.file_field.name.replace(upload_to+'/','')

    def get_full_path(self):
        return upload_to + self.file_field.name

def Comment(models.Model):
    content = models.CharField(max_length=100, blank=False)

    account = models.ForeignKey(Account, blank=True, null=True)
    like_account = models.ManyToManyField(Account, blank=True, null=True)

    picture = models..ForeignKey(Picture, null=False)

    def __unicode__(self):
        return self.account.username + self.content

class Tag(models.Model):
    name = models.CharField(max_length=200)
    created_at  = models.DateTimeField(auto_now_add=True)

    account = models.ForeignKey(Account, null=True)

    def __unicode__(self):
        return self.name

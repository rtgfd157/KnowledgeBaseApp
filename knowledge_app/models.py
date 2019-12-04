from django.db import models
from django.conf import settings

class Subject(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField()
    subject_field = models.ForeignKey(to='Subject', on_delete=models.CASCADE, blank=True, null=True,
                                        verbose_name ='subject')
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=255, unique=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                related_name="subjects")

    def __str__(self):
        return self.title

class Comment(models.Model):
    updated_at = models.DateTimeField(auto_now=True)
    comment_title = models.CharField(max_length=160, blank=False, null=False)
    comment_description = models.TextField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="comments")


    def __str__(self):
        return self.comment_title

class Url_Link(models.Model):
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=160, blank=False, null=False)
    description = models.TextField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="url_links")
    url_link = models.CharField(blank=False, null=False,max_length=200)

    def __str__(self):
        return self.title + " " + self.url_link


class CodeBlock(models.Model):
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=160, blank=False, null=False)
    description = models.TextField()
    #code_langauge= models.CharField(max_length=60, blank=False, null=False)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="code_block")
    code = models.TextField()

    def __str__(self):
        return self.title 
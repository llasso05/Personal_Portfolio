from django.db import models

# Create your models here.


class Blog(models.Model):
    blog_title = models.CharField(max_length=250)
    blog_date = models.DateField()
    blog_text = models.TextField()

    # This function returns the name at the admin page
    def __str__(self):
        return (self.blog_title)


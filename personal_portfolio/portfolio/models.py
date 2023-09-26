from django.db import models

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=100) #defines character field
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)

    # This function returns the name at the admin page
    def __str__(self):
        return (self.title)


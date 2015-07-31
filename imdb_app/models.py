from django.db import models

# Create your models here.

USER_ACCESS = (('Normal', 'Normal'),
               ('Admin', 'Admin'),)


class GenreCategory(models.Model):
    """ This class will have all the Genre type listed.
    """
    genre_type = models.CharField(max_length=50, blank=False)

    def __unicode__(self):
        return "%s" %self.genre_type


class MovieDetails(models.Model):
    """ This class hold the data of the Movies Details.
    """
    name = models.CharField(max_length=100, blank=False)
    imdb_score = models.IntegerField()
    popularity = models.IntegerField()
    director = models.CharField(max_length=100, blank=False)
    genre = models.ManyToManyField(GenreCategory)

    def __unicode__(self):
        return "%s-%s" %(self.name, self.director)

    # class Meta:
    #     ordering = ('-popularity',)

class UserProfile(models.Model):
    """ This class hold the data the User Profile information.
    """
    email_id = models.EmailField(blank=False)
    password = models.CharField(blank=False, max_length=50)
    name = models.CharField(blank=False, max_length=100)
    last_name = models.CharField(max_length=100)
    access_type = models.CharField(choices=USER_ACCESS, max_length=50)

    def __unicode__(self):
        return "%s-%s" %(self.email_id, self.access_type)
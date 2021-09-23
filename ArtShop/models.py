from django.db import models


class Category(models.Model):
    '''
    We may need to add a description field for this model but for now we will only use the name field. 
    '''
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class ArtPiece(models.Model):
    '''
    This is the model for the art pieces.
    '''
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    #There should be an image field for this model but not sure how which way to do this.
    #More than likely going to have a media folder and have the images in there.
    image = models.ImageField(upload_to='media/', blank=True)

    def __str__(self):
        return self.name
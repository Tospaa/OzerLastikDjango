from django.db import models

class Ayakkabi(models.Model):
    Numara = models.IntegerField()
    Adet = models.IntegerField()

    def __str___(self):
        return "{0} numara ayakkabı".format(self.Numara)

    def __repr___(self):
        return "{0} numara ayakkabı repr".format(self.Numara)

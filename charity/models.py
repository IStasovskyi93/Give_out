from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=60, verbose_name='Kategoria')

    def __str__(self):
        return self.name


class Institution(models.Model):
    name = models.CharField(max_length=100, verbose_name='Instytucja')
    description = models.TextField()
    type = models.CharField(verbose_name='Wybierz typ', choices=(('fundacja', 'Fundacja'),
                            ('organ. pazarządowa', 'Organizacja pozarządowa'), ('zbiórka lokalna', 'Zbiórka lokalna')),
                            default='Fundacja', max_length=100)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.name


class Donation(models.Model):
    quantity = models.IntegerField()
    categories = models.ManyToManyField(Category)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    address = models.CharField(max_length=150)
    phone_number = models.PositiveSmallIntegerField()
    city = models.CharField(max_length=60)
    zip_code = models.IntegerField()
    pick_up_date = models.DateField()
    pick_up_time = models.TimeField()
    pick_up_comment = models.TextField()
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)



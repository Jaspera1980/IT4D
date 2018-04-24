from django.db import models
from django.utils import timezone

class AniRegForm(models.Model):
    veterinarian = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    registration_date = models.DateTimeField(default=timezone.now)
    animals = (
        ('CKN', 'Chicken'),
        ('FWL', 'Fowl'),
        ('DCK', 'Duck'),
        ('TKY', 'Turkey'),
        ('OTH', 'Other bird'),
    )
    animale_type = models.CharField(max_length=3, choices=animals)
    diseases = (
        ('NC', 'Newcastle Disease'),
        ('FP', 'Fowl Pox'),
        ('IB', 'Infectious Bursal Disease'),
        ('MD', 'Mareks Disease'),
        ('OD', 'Other Disease'),
    )
    disease_type = models.CharField(max_length=2, choices=diseases)
    treatment_1 = models.TextField(default=' ')
    treatment_date = models.DateTimeField(blank=True, null=True)
    comments = models.TextField(default=' ')



    def treatment(self):
        self.treatment_date = timezone.now()
        self.save()

    def __str__(self):
        return self.animale_type + self.disease_type


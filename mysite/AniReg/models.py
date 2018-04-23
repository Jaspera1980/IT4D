from django.db import models
from django.utils import timezone

class AniRegForm(models.Model):
    veterinarian = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    animals = (
        ('CHICKEN', 'Chicken'),
        ('FOWL', 'Fowl'),
        ('DUCK', 'Duck'),
        ('TURKEY', 'Turkey'),
        ('OTHER', 'Other bird'),
    )
    animale_type = models.CharField(max_length=1, choices=animals)
    diseases = (
        ('NC', 'Newcastle Disease'),
        ('FP', 'Fowl Pox'),
        ('IBD', 'Infectious Bursal Disease'),
        ('MD', 'Mareks Disease'),
        ('OD', 'Other Disease'),
    )
    disease_type = models.CharField(max_length=1, choices=diseases)
    treatment = models.TextField()
    registration_date = models.DateTimeField(default=timezone.now)
    treatment_date = models.DateTimeField(blank=True, null=True)
    comments = models.TextField()

    def treatment(self):
        self.treatment_date = timezone.now()
        self.save()

    def __str__(self):
        return self.animale_type + self.disease_type





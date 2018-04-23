from django.db import models
from django.utils import timezone

class AniRegForm(models.Model):
    veterinarian = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    animale_type = models.CharField(max_length=50)
    disease_type = models.CharField(max_length=50)
    treatment = models.TextField()
    registration_date = models.DateTimeField(default=timezone.now)
    treatment_date = models.DateTimeField(blank=True, null=True)

    def treatment(self):
        self.treatment_date = timezone.now()
        self.save()

    def __str__(self):
        return self.animale_type + self.disease_type





from django.db import models

# Create your models here.

class RentalModel(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class ReservationModel(models.Model):
    rental_name = models.ForeignKey(RentalModel, on_delete=models.CASCADE, related_name="rentals")
    checkin = models.DateField()
    checkout = models.DateField()

    def __str__(self):
        return f"Res-{self.id} ID"
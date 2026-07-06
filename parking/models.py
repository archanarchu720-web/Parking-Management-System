from django.db import models

class Parking(models.Model):
    STATUS = [
        ('Parked', 'Parked'),
        ('Free', 'Free')
    ]

    vehicle_type = models.CharField(max_length=50)
    vehicle_number = models.CharField(max_length=30)
    owner_name = models.CharField(max_length=100)
    parked_hours = models.IntegerField()
    paid_amount = models.FloatField()
    status = models.CharField(max_length=10, choices=STATUS)

    def __str__(self):
        return self.vehicle_number
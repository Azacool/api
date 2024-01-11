from django.db import models

class Branch(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name

class Employee(models.Model):
    profession = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

class Car(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    color = models.CharField(max_length=50)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

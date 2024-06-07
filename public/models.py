from django.db import models


class ContactRequest(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    email = models.EmailField(max_length=100)
    message = models.TextField(null=True)

    def __str__(self) -> str:
        return f"Name: {self.name} / Phone: {self.phone}"



class EstimateRequest(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    email = models.EmailField(max_length=100)
    message = models.TextField(null=True)

    def __str__(self) -> str:
        return f"Name: {self.name} / Phone: {self.phone}"




from django.db import models
from django.core.validators import MinLengthValidator


class Make(models.Model):
    name = models.CharField(
            max_length=200,
            help_text='Enter a make (e.g. Hyundai)',
            validators=[MinLengthValidator(3, "Make must be greater than 2 character")]
    )

    def __str__(self):
        """String for representing the Model object."""
        return self.name


class Auto(models.Model):
    nickname = models.CharField(
            max_length=200,
            validators=[MinLengthValidator(3, "Nickname must be greater than 2 character")]
    )
    mileage = models.PositiveIntegerField()
    comments = models.CharField(max_length=300)
    make = models.ForeignKey('Make', on_delete=models.CASCADE, null=False)

    # Shows up in the admin list
    def __str__(self):
        return self.nickname
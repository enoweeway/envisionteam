from django.db import models

class Nurse(models.Model):

    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
        ('Prefer not to say', 'Prefer not to say')
    )

    lastName = models.CharField(max_length=100, null=True)
    firstName = models.CharField(max_length=100, null=True)
    middleName = models.CharField(max_length=100, null=True)
     
    homeAddress = models.TextField(max_length=255, null=True)
    medicalSchool = models.CharField(max_length=100, null=True)

    email = models.EmailField(max_length=200, null=True, unique=True)
    gender = models.CharField(max_length=30, null=True, choices=GENDER)
    contactNumber = models.CharField(max_length=200, null=True)

    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.lastName + ', ' + self.firstName + ' ' + self.middleName
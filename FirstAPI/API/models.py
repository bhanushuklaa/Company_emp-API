from django.db import models

# Create your models here.
# creating company model


class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=50)
    about = models.TextField()
    type = models.CharField(
        max_length=100, choices=(("IT", "IT"), ("Non IT", "Non IT"))
    )
    added_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name + " - " + self.location


# creating employee list


class Employee(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=11)
    about = models.TextField()
    position = models.CharField(
        max_length=50,
        choices=(
            ("Manager", "Manager"),
            ("Software Developer", "Software Developer"),
            ("Testing", "Testing"),
            ("Project Leader", "Project Leader"),
            ("Intern", "Intern"),
        ),
    )
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

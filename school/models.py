from django.db import models

# Create your models here.


class Header(models.Model):
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='header/')

    def __str__(self):
        return self.title



class Role(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name



class Employee(models.Model):
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name




class SchoolClasses(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='classes/')
    price = models.IntegerField()
    teacher = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)
    capacity = models.IntegerField(default=0)

    def __str__(self):
        return self.full_name



class Age(models.Model):
    age = models.IntegerField()
    school_classes = models.ForeignKey(SchoolClasses, on_delete=models.CASCADE)

    def __str__(self):
        return self.age


class Time(models.Model):
    time = models.TimeField()
    school_classes = models.ForeignKey(SchoolClasses, on_delete=models.CASCADE)

    def __str__(self):
        return self.time
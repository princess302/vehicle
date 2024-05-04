from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Customer(models.Model):  # This is now representing a Driver
    EMPLOYMENT_STATUS_CHOICES = [
        ('FT', 'Full Time'),
        ('PT', 'Part Time'),
        ('C', 'Contract'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pic/CustomerProfilePic/', null=True, blank=True)  # Consider renaming the upload_to path
    address = models.CharField(max_length=40, default='N/A')
    mobile = models.CharField(max_length=20, null=False)
    employee_id = models.CharField(max_length=20, unique=True, default='N/A')
    employment_status = models.CharField(max_length=2, choices=EMPLOYMENT_STATUS_CHOICES, default='FT')
    driver_license_number = models.CharField(max_length=20, unique=True, default='N/A')

    # existing methods...


class Mechanic(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='profile_pic/MechanicProfilePic/',null=True,blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=False)
    skill = models.CharField(max_length=500,null=True)
    salary=models.PositiveIntegerField(null=True)
    status=models.BooleanField(default=False)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return self.user.first_name


class Request(models.Model):
    VEHICLE_CATEGORY_CHOICES = [
        ('two wheeler with gear', 'two wheeler with gear'),
        ('two wheeler without gear', 'two wheeler without gear'),
        ('three wheeler', 'three wheeler'),
        ('four wheeler', 'four wheeler')
    ]

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Repairing', 'Repairing'),
        ('Repairing Done', 'Repairing Done'),
        ('Released', 'Released')
    ]

    category = models.CharField(max_length=50, choices=VEHICLE_CATEGORY_CHOICES)
    vehicle_no = models.PositiveIntegerField(null=False)
    vehicle_name = models.CharField(max_length=40, null=False)
    vehicle_model = models.CharField(max_length=40, null=False)
    vehicle_brand = models.CharField(max_length=40, null=False)
    problem_description = models.CharField(max_length=500, null=False)
    date = models.DateField(auto_now=True)
    cost = models.PositiveIntegerField(null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    mechanic = models.ForeignKey('Mechanic', on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending', null=True)

    def __str__(self):
        return self.problem_description

class Attendance(models.Model):
    mechanic=models.ForeignKey('Mechanic',on_delete=models.CASCADE,null=True)
    date=models.DateField()
    present_status = models.CharField(max_length=10)

class Feedback(models.Model):
    date=models.DateField(auto_now=True)
    by=models.CharField(max_length=40)
    message=models.CharField(max_length=500)


    
class Vehicle(models.Model):
    STATUS_CHOICES = [
        ('A', 'Active'),
        ('I', 'Inactive'),
        ('M', 'Under Maintenance'),
    ]

    registration_number = models.CharField(max_length=20, unique=True)
    make_model = models.CharField(max_length=40)
    fuel_type = models.CharField(max_length=20)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)

class Route(models.Model):
    route_id = models.CharField(max_length=20, unique=True)
    origin = models.CharField(max_length=40)
    destination = models.CharField(max_length=40)
    distance = models.PositiveIntegerField()
    estimated_travel_time = models.PositiveIntegerField()

class Customer(models.Model):  # This is now representing a Driver
    EMPLOYMENT_STATUS_CHOICES = [
        ('FT', 'Full Time'),
        ('PT', 'Part Time'),
        ('C', 'Contract'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pic/CustomerProfilePic/', null=True, blank=True)  # Consider renaming the upload_to path
    address = models.CharField(max_length=40, default='N/A')
    mobile = models.CharField(max_length=20, null=False)
    employee_id = models.CharField(max_length=20, unique=True, default='N/A')
    employment_status = models.CharField(max_length=2, choices=EMPLOYMENT_STATUS_CHOICES, default='FT')
    driver_license_number = models.CharField(max_length=20, unique=True, default='N/A')

    class Vehicle(models.Model):
        STATUS_CHOICES = [
            ('A', 'Active'),
            ('I', 'Inactive'),
            ('M', 'Under Maintenance'),
        ]

        registration_number = models.CharField(max_length=20, unique=True)
        make_model = models.CharField(max_length=40)
        fuel_type = models.CharField(max_length=20)
        status = models.CharField(max_length=1, choices=STATUS_CHOICES)

class Route(models.Model):
    route_id = models.CharField(max_length=20, unique=True)
    origin = models.CharField(max_length=40)
    destination = models.CharField(max_length=40)
    distance = models.PositiveIntegerField()
    estimated_travel_time = models.PositiveIntegerField()



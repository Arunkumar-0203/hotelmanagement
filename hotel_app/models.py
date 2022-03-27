from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.db import models

# Create your models here.
class UserType(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    type = models.CharField(max_length=50)

class customer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    contact = models.CharField(max_length=100,null=True)
    Address = models.CharField(max_length=100,null=True)
    emil = models.CharField(max_length=100,null=True)
    dob = models.CharField(max_length=100,null=True)
    id_proof= models.ImageField('images/',null=True)
    place = models.CharField(max_length=100,null=True)
    district = models.CharField(max_length=100,null=True)
    nation = models.CharField(max_length=100,null=True)
    status = models.CharField(max_length=100,null=True)

class Hotelss(models.Model):
    Name = models.CharField(max_length=100,null=True)
    Image = models.ImageField('images/',null=True)
    Place = models.CharField(max_length=100,null=True)
    Status = models.CharField(max_length=100,null=True)
    status1 = models.CharField(max_length=100 ,null=True,default='0')

class Manager( models.Model):
    Userr = models.ForeignKey(User,on_delete=models.CASCADE)
    hotel= models.ForeignKey(Hotelss,on_delete=models.CASCADE,null=True)
    Contact = models.CharField(max_length=100,null=True)
    Address = models.CharField(max_length=100,null=True)
    Emil = models.CharField(max_length=100,null=True)
    Dob = models.CharField(max_length=100,null=True)
    Id_proof= models.ImageField('images/',null=True)
    Place = models.CharField(max_length=100,null=True)
    District = models.CharField(max_length=100,null=True)
    status = models.CharField(max_length=100,null=True)

class RoomType(models.Model):
    roomtype=models.CharField(max_length=100,null=True)
    Details = models.CharField(max_length=100,null=True)
    Hotel =models.ForeignKey(Hotelss,on_delete=models.CASCADE,null=True)
    images=models.ImageField('image/',null=True)
    status=models.CharField(max_length=100,null=True)

class facility(models.Model):
    Facility = models.CharField(max_length=100,null=True)
    status = models.CharField(max_length=100,null=True)
    price = models.CharField(max_length=100,null=True)
    # Hotels =models.ForeignKey(Hotelss,on_delete=models.CASCADE,null=True)

class Rooms(models.Model):
    HOTEL = models.ForeignKey(Hotelss,on_delete=models.CASCADE,null=True)
    roomtype= models.ForeignKey(RoomType,on_delete=models.CASCADE,null=True)
    Price = models.CharField(max_length=100,null=True)
    total =  models.CharField(max_length=100,null=True)
    status =  models.CharField(max_length=100,null=True)
class Reservation(models.Model):
    Customer = models.ForeignKey(customer,on_delete=models.CASCADE,null=True)
    users = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    ROOM = models.ForeignKey(Rooms,on_delete=models.CASCADE,null=True)
    check_in_time = models.CharField(max_length=100,null=True)
    check_in_date = models.CharField(max_length=100,null=True)
    check_out_time = models.CharField(max_length=100,null=True)
    check_out_date = models.CharField(max_length=100,null=True)
    status =  models.CharField(max_length=100,null=True)
    manager =  models.CharField(max_length=100,null=True)
    status1 =  models.CharField(max_length=100,null=True)
    status2 =  models.CharField(max_length=100,null=True,default='null')


class facilityselected(models.Model):
    Users = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    Reserve = models.ForeignKey(Reservation,on_delete=models.CASCADE,null=True)
    statuss =  models.CharField(max_length=100,null=True)
    facilityy = ArrayField(models.CharField(max_length=100,null=True),size=10,default=list,null=True)

class payment(models.Model):
    userr = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    Customers = models.ForeignKey(customer,on_delete=models.CASCADE,null=True)
    MANAGER = models.ForeignKey(Manager,on_delete=models.CASCADE,null=True)
    status =models.CharField(max_length=100,null=True)
    room = models.ForeignKey(Rooms,on_delete=models.CASCADE,null=True)
    price = models.CharField(max_length=100,null=True)
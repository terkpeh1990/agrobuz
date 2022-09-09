from django.db import models
from django.conf import settings
from simple_history.models import HistoricalRecords
from crum import get_current_user
from .utils import incrementor,revenue_incrementor


User = settings.AUTH_USER_MODEL
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(
        User, blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    telephone = models.CharField(max_length=20,null=True, blank=True)

    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_new = models.BooleanField(default=False)

    history = HistoricalRecords()

    def __str__(self):
        return self.name


class AllLogin(models.Model):
    st = (
        ('Logged In', 'Logged In'),
        ('Logged Out', 'Logged Out'),

    )
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    status = models.CharField(max_length=255,choices=st,null=True, blank=True)
    date= models.DateTimeField(auto_now_add= True)

    history = HistoricalRecords()


    def __str__(self):
        return str(self.user) + ': ' + str(self.date)


class Location(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ('name',)

    history = HistoricalRecords()

    def __str__(self):
        return self.name



class Sex(models.Model):
    name = models.CharField(max_length=50)

    history = HistoricalRecords()

    def __str__(self):
        return self.name

class Marital_Status(models.Model):
    name = models.CharField(max_length=50)

    history = HistoricalRecords()

    def __str__(self):
        return self.name

class Value_Chain(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ('name',)

    history = HistoricalRecords()

    def __str__(self):
        return self.name


class Bio_Data(models.Model):

    id = models.CharField(max_length=100, primary_key=True)
    first_name = models.CharField(max_length=250)
    surname = models.CharField(max_length=250)
    other_name = models.CharField(max_length=250,null=True,blank=True)
    dob = models.DateField(null=True,blank=True)
    sex = models.ForeignKey(Sex, on_delete=models.CASCADE)
    marital_status = models.ForeignKey(Marital_Status, on_delete=models.CASCADE,null=True,blank=True)
    valid_id = models.CharField(max_length=250,null=True,blank=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    contact = models.CharField(max_length=12,null=True,blank=True)

    value_chain = models.ForeignKey(Value_Chain, on_delete=models.CASCADE)
    log = models.ForeignKey(AllLogin, on_delete=models.CASCADE,null=True,blank=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.first_name

    def save(self, *args, **kwargs):
        if not self.id:
            number = incrementor()
            self.id = "ATT" + str(number())
            while Bio_Data.objects.filter(id=self.id).exists():
                self.id = "ATT" + str(number())
        super(Bio_Data, self).save(*args, **kwargs)


class Crops(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ('name',)

    history = HistoricalRecords()

    def __str__(self):
        return self.name

class Animals(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ('name',)

    history = HistoricalRecords()

    def __str__(self):
        return self.name


class Crop_Farming(models.Model):
    bio = models.ForeignKey(Bio_Data, on_delete=models.CASCADE)
    crop=models.ForeignKey(Crops, on_delete=models.CASCADE)
    size = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    current_yields = models.PositiveIntegerField(default=0)
    longitude = models.DecimalField(max_digits=15, decimal_places=10,null=True,blank=True)
    latitude = models.DecimalField(max_digits=15, decimal_places=10,null=True,blank=True)
    log = models.ForeignKey(AllLogin, on_delete=models.CASCADE,null=True,blank=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.crop.name


class CropFarming_Yeild(models.Model):
    crop_farming=models.ForeignKey(Crop_Farming, on_delete=models.CASCADE)
    yield_date = models.DateField(auto_now_add=True)
    yields = models.PositiveIntegerField(default=0)
    log = models.ForeignKey(AllLogin, on_delete=models.CASCADE,null=True,blank=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.yields


class Animal_Farming(models.Model):
    bio = models.ForeignKey(Bio_Data, on_delete=models.CASCADE)
    animal=models.ForeignKey(Animals, on_delete=models.CASCADE)
    number = models.PositiveIntegerField(default=0)
    longitude = models.DecimalField(max_digits=15, decimal_places=10,null=True,blank=True)
    latitude = models.DecimalField(max_digits=15, decimal_places=10,null=True,blank=True)
    log = models.ForeignKey(AllLogin, on_delete=models.CASCADE,null=True,blank=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.animal.name

class AnimalFarming_Yeild(models.Model):
    animal_farming=models.ForeignKey(Animal_Farming, on_delete=models.CASCADE)
    yield_date = models.DateField(auto_now_add=True)
    number = models.PositiveIntegerField(default=0)

    history = HistoricalRecords()

    def __str__(self):
        return self.number





class Business_Info(models.Model):
    st = (
        ('Yes', 'Yes'),
        ('No', 'No'),

    )
    wn = (
        ('Single Ownership', 'Single Ownership'),
        ('Multi Ownership', 'Multi Ownership'),

    )
    sc = (
        ('Small Scale', 'Small Scale'),
        ('Medium Scale', 'Medium Scale'),
        ('Large Scale', 'Large Scale'),

    )
    lts = (
        ('Registered', 'Registered'),
        ('Unregistered', 'Unregistered'),

    )
    id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=255)
    permit = models.CharField(max_length=255,null=True,blank=True)
    tin_number = models.CharField(max_length=255,null=True,blank=True)
    value_chain = models.ForeignKey(Value_Chain, on_delete=models.CASCADE)
    permanent_staff_no = models.PositiveIntegerField(default=0)
    casual_staff_no = models.PositiveIntegerField(default=0)
    registration_status = models.CharField(max_length=255,choices=st)
    type_ownership = models.CharField(max_length=255,choices=wn,default='Single Ownership')
    scale = models.CharField(max_length=255,choices=sc)
    led_by_woman = models.CharField(max_length=255,choices=st,default='No')
    bio = models.ForeignKey(Bio_Data, on_delete=models.CASCADE,null=True,blank=True)
    total_land_area_of_farm = models.PositiveIntegerField(default=0)
    total_area_under_cultivation = models.PositiveIntegerField(default=0)
    land_title_status = models.CharField(max_length=255,choices=lts,default='Registered')
    longitude = models.DecimalField(max_digits=15, decimal_places=10,null=True,blank=True)
    latitude = models.DecimalField(max_digits=15, decimal_places=10,null=True,blank=True)
    log = models.ForeignKey(AllLogin, on_delete=models.CASCADE,null=True,blank=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            number = incrementor()
            self.id = "ATTBUS" + str(number())
            while Business_Info.objects.filter(id=self.id).exists():
                self.id = "ATTBUS" + str(number())
        super(Business_Info, self).save(*args, **kwargs)


class Business_Partners(models.Model):
    bio = models.ForeignKey(Bio_Data, on_delete=models.CASCADE)
    business=models.ForeignKey(Business_Info, on_delete=models.CASCADE)

    history = HistoricalRecords()

    def __str__(self):
        return self.business.name



class Type_of_association (models.Model):
    name = models.CharField(max_length=100)

    history = HistoricalRecords()

    def __str__(self):
        return self.name

class Associations(models.Model):
    name = models.CharField(max_length=250)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    male_members = models.PositiveIntegerField(default=0)
    female_members = models.PositiveIntegerField(default=0)
    contact = models.CharField(max_length=12)
    value_chain = models.ForeignKey(Value_Chain, on_delete=models.CASCADE)
    log = models.ForeignKey(AllLogin, on_delete=models.CASCADE,null=True,blank=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.name


class Bio_Association(models.Model):
    st = (
        ('Executive', 'Executive'),
        ('Member', 'Member'),

    )
    bio = models.ForeignKey(Bio_Data, on_delete=models.CASCADE)
    association = models.ForeignKey(Associations, on_delete=models.CASCADE)
    role = models.CharField(max_length=255,choices=st)
    log = models.ForeignKey(AllLogin, on_delete=models.CASCADE,null=True,blank=True)

    history = HistoricalRecords()

    def __str__(self):
        return self.bio.first_name


class Other_value_production(models.Model):
    business = models.ForeignKey(Business_Info, on_delete=models.CASCADE)
    total_production = models.CharField(max_length=250,null=True,blank=True)

    history = HistoricalRecords()

    def __str__(self):
        return self.bio.first_name


class Ica_code(models.Model):
    code  = models.CharField(max_length=250,null=True,blank=True)
    description = models.CharField(max_length=1000,null=True,blank=True)
    sub_code  = models.CharField(max_length=250,null=True,blank=True)
    sub_description = models.CharField(max_length=1000,null=True,blank=True)

    def __str__(self):
        return self.code + '---' + self.description + '---' + self.sub_code+'---'+self.sub_description


class Business_ic(models.Model):
    business = models.ForeignKey(Business_Info, on_delete=models.CASCADE)
    code = models.ForeignKey(Ica_code, on_delete=models.CASCADE)

    def __str__(self):
        return self.code.description



class Grouping_name(models.Model):
    name = models.CharField(max_length=300, null=True,blank=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.name

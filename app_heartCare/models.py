from django.db import models

# Create your models here.
EXPERIENCE_CHOICE = (
    ('1','One'),
    ('2','Two'),
    ('3','Three'),
    ('4','Four'),
    ('5','Five')
    
)

GENDER_CHOICE = (
    ('M','Male'),
    ('F','Female')


)

class Nurse(models.Model):
    
    Name = models.CharField(max_length=50)
    img = models.ImageField(upload_to='Nurse')
    Email = models.EmailField()
    Phone = models.IntegerField()
    Address = models.TextField()
    Experience = models.CharField(choices=EXPERIENCE_CHOICE,  max_length=1)
    Qualification = models.CharField(max_length=50)
    WorkingDays = models.IntegerField()
    
    Hospital= models.ForeignKey(
        'Hospital',
        on_delete=models.CASCADE

        )
    Gender = models.CharField(choices = GENDER_CHOICE,  max_length=1)
    FeesPerDay = models.IntegerField()

    def __str__(self):
        return self.Name



class Hospital(models.Model):
    
    Name = models.CharField(max_length=50)


    def __str__(self):
        return self.Name


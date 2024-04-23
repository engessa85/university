from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models
from django.conf import settings
from datetime import date

class UserAccountManager(BaseUserManager):
    def create_user(self, username, email, password=None, civilID=None):

        user = self.model(
            username=username,
            email=self.normalize_email(email),
            civilID=civilID
        )


        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, email, password=None, civilID=None):
        user = self.create_user(
            username=username,
            email=email,
            password=password,
            civilID=civilID
        )

        user.is_active = True
        user.is_staff = True
        user.is_superuser = True

        user.is_student = True
        user.is_university = True

        user.save(using=self._db)
        return user

class UserAccount(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    civilID = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_university = models.BooleanField(default=False)
    
    objects = UserAccountManager()

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email', 'civilID']


    def get_full_name(self):
        return self.email
    
    def get_short_name(self):
        return self.email
    
    def __str__(self):
        return self.email
    

class UniversityUser(UserAccount):
    universityname = models.CharField(max_length=255, blank=True, null=True)




class UniversityData(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    speciamain = models.CharField(max_length=255, null = True, blank= True)
    about_university = models.TextField(null = True, blank= True)
    score1 = models.FloatField(null = True, blank= True)
    score2 = models.FloatField(null = True, blank= True)
    score3 = models.FloatField(null = True, blank= True)
    score4 = models.FloatField(null = True, blank= True)
    score5 = models.FloatField(null = True, blank= True)
    score6 = models.FloatField(null = True, blank= True)
    specialization1 = models.CharField(max_length=255, null = True, blank= True)
    seats1 = models.IntegerField(null = True, blank= True)
    college1 = models.CharField(max_length=255, null = True, blank= True)
    acceptance_rate1 = models.FloatField(null = True, blank= True)

   









class Student(models.Model):
    userstudent = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    studentemail = models.EmailField(null=True, blank=True)
    fathernamearabic = models.CharField(max_length=255, null=True, blank=True)
    familynamearabic = models.CharField(max_length=255, null=True, blank=True)
    fathernameenglish = models.CharField(max_length=255, null=True, blank=True)
    familynameenglish = models.CharField(max_length=255, null=True, blank=True)
    nationality = models.CharField(max_length=255, null=True, blank=True)
    StudentID = models.CharField(max_length=255, null=True, blank=True)
    firstnamearabic = models.CharField(max_length=255, null=True, blank=True)
    grandfathernamearabic = models.CharField(max_length=255, null=True, blank=True)
    firstnameenglish = models.CharField(max_length=255, null=True, blank=True)
    grandfathernameenglish = models.CharField(max_length=255, null=True, blank=True)
    nationality1 = models.CharField(max_length=255, null=True, blank=True)
    phonenumber = models.CharField(max_length=255, null=True, blank=True)
    malegender = models.BooleanField(null=True, blank=True)
    femalegender = models.BooleanField(null=True, blank=True)
    autism = models.BooleanField(null=True, blank=True)
    Visualimpairment = models.BooleanField(null=True, blank=True)
    learningdifficulties = models.BooleanField(null=True, blank=True)
    psychological = models.BooleanField(null=True, blank=True)
    Withoutdisabilit = models.BooleanField(null=True, blank=True)
    Movementdisorder = models.BooleanField(null=True, blank=True)
    CommunicationDisorders = models.BooleanField(null=True, blank=True)
    Hearingimpairment = models.BooleanField(null=True, blank=True)
    Physicalhealthdisability = models.BooleanField(null=True, blank=True)
    Birtharea = models.CharField(max_length=255, null=True, blank=True)
    Cityofbirth = models.CharField(max_length=255, null=True, blank=True)
    birthdate = models.DateField(null=True, blank=True)

    countryofbirth = models.CharField(max_length=255, null=True, blank=True)
    no = models.BooleanField(null=True, blank=True)
    yes = models.BooleanField(null=True, blank=True)
    Jobtitle = models.CharField(max_length=255, null=True, blank=True)
    privatesector = models.BooleanField(null=True, blank=True)
    governmentsector = models.BooleanField(null=True, blank=True)
    jobstate = models.BooleanField(null=True, blank=True)
    jobplace = models.CharField(max_length=255, null=True, blank=True)
    relativerelation = models.CharField(max_length=255, null=True, blank=True)
    phone1 = models.CharField(max_length=255, null=True, blank=True)
    fathersnameistriple = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    address1 = models.CharField(max_length=255, null=True, blank=True)
    Emergincypersonname = models.CharField(max_length=255, null=True, blank=True)
    phone2 = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    yearofstudy = models.CharField(max_length=255, null=True, blank=True)
    Cumulativeaverage = models.CharField(max_length=255, null=True, blank=True)
    achievetest = models.CharField(max_length=255, null=True, blank=True)
    area = models.CharField(max_length=255, null=True, blank=True)
    school = models.CharField(max_length=255, null=True, blank=True)
    highschooltype = models.CharField(max_length=255, null=True, blank=True)
    cognitivetest = models.CharField(max_length=255, null=True, blank=True)
    mentionit = models.CharField(max_length=255, null=True, blank=True)
    certificate = models.CharField(max_length=255, null=True, blank=True)
    college = models.CharField(max_length=255, null=True, blank=True)
    gender = models.BooleanField(null=True, blank=True)
    gender_m = models.BooleanField(null=True, blank=True)
    gender_f = models.BooleanField(null=True, blank=True)
    universityname = models.CharField(max_length=255, null=True, blank=True)

    def save(self, *args, **kwargs):
        # Set default value for birthdate if it's None
        if self.birthdate is None:
            self.birthdate = date.today()
        
        super(Student, self).save(*args, **kwargs)

    def __str__(self):
        return self.studentemail  # or any other field you want to be displayed


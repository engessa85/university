from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models
from django.conf import settings

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




class StudentMoreInfo(models.Model):
    studentUser = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    # Basic student information
    studentemail = models.EmailField(verbose_name="البريد الالكتروني", null=False, blank=False)
    fathernamearabic = models.CharField(max_length=255, verbose_name="اسم الاب بالعربيه", null=False, blank=False)
    familynamearabic = models.CharField(max_length=255, verbose_name="اسم العائله بالعربيه", null=False, blank=False)
    fathernameenglish = models.CharField(max_length=255, verbose_name="اسم الاب بالانجليزيه", null=False, blank=False)
    familynameenglish = models.CharField(max_length=255, verbose_name="اسم العائله بالانجليزيه", null=False, blank=False)
    nationality = models.CharField(max_length=255, verbose_name="دوله الجنسيه", null=False, blank=False)
    StudentID = models.CharField(max_length=255, verbose_name="رقم الهويه الوطنيه", null=False, blank=False)
    firstnamearabic = models.CharField(max_length=255, verbose_name="الاسم الاول بالعربيه", null=False, blank=False)
    grandfathernamearabic = models.CharField(max_length=255, verbose_name="اسم الجد بالعربيه", null=False, blank=False)
    firstnameenglish = models.CharField(max_length=255, verbose_name="الاسم الاول بالانجليزيه", null=False, blank=False)
    grandfathernameenglish = models.CharField(max_length=255, verbose_name="اسم الجد بالانجليزيه", null=False, blank=False)
    nationality1 = models.CharField(max_length=255, verbose_name="الجنسيه", null=False, blank=False)
    phonenumber = models.CharField(max_length=255, verbose_name="رقم الجوال", null=False, blank=False)
    malegender = models.BooleanField(verbose_name="ذكر", default=True)
    femalegender = models.BooleanField(verbose_name="انثى", default=False)

    # Disability information
    autism = models.BooleanField(verbose_name="اضطرابات التوحد", default=False, null=False)
    Visualimpairment = models.BooleanField(verbose_name="اعاقه بصريه", default=False, null=False)
    learningdifficulties = models.BooleanField(verbose_name="صعوبات التعلم", default=False, null=False)
    psychological = models.BooleanField(verbose_name="اضطربات نفسيه", default=False, null=False)
    Withoutdisabilit = models.BooleanField(verbose_name="بدون اعاقه", default=False, null=False)

    Movementdisorder = models.BooleanField(verbose_name="اضطربات فدط الحدكه", default=False, null=False)
    CommunicationDisorders = models.BooleanField(verbose_name="اضطربات التواصل", default=False, null=False)
    Hearingimpairment = models.BooleanField(verbose_name="اعاقه سمعيه", default=False, null=False)
    Physicalhealthdisability = models.BooleanField(verbose_name="اعاقه بدنيه وصحيه", default=False, null=False)

    # Birth information
    Birtharea = models.CharField(max_length=255, verbose_name="منطقه الميلاد", null=False, blank=False)
    Cityofbirth = models.CharField(max_length=255, verbose_name="محل الميلاد - المدينه", null=False, blank=False)
    birthdate = models.DateField(verbose_name="تاريخ الميلاد", null=False, blank=False)
    countryofbirth = models.CharField(max_length=255, verbose_name="محل الميلاد - الدوله", null=False, blank=False)
    sonOfmartyrs = models.BooleanField(verbose_name="هل انت ابن/ابنه احد شهداء الواجب", default=False, null=False)
    Age = models.IntegerField(verbose_name="عمر المتقدم / المتقدمه", null=False, blank=False)

    # Work information
    Jobtitle = models.CharField(max_length=255, verbose_name="المسمي الوظيفي", null=True)
    jobstate = models.CharField(max_length=255, verbose_name="الحاله الوظيفيه", null=True)
    jobplace = models.CharField(max_length=255, verbose_name="جه العمل", null=True)

    # Guardian information
    relativerelation = models.CharField(max_length=255, verbose_name="صله القرابه", null=False, blank=False)
    phone1 = models.CharField(max_length=255, verbose_name="الجوال", null=False, blank=False)
    fathersnameistriple = models.CharField(max_length=255, verbose_name="اسم ولي الامر ثلاثي", null=False, blank=False)
    address = models.CharField(max_length=255, verbose_name="العنوان", null=False, blank=False)

    # Emergency contact information
    address1 = models.CharField(max_length=255, verbose_name="العنوان", null=False, blank=False)
    Emergincypersonname = models.CharField(max_length=255, verbose_name="اسم شخص للطوارئ", null=False, blank=False)
    phone2 = models.CharField(max_length=255, verbose_name="رقم الجوال", null=False, blank=False)

    # Secondary certificate information
    city = models.CharField(max_length=255, verbose_name="المدينه", null=False, blank=False)
    yearofstudy = models.IntegerField(verbose_name="العام الدراسي", null=False, blank=False)
    Cumulativeaverage = models.FloatField(verbose_name="المعدل التداكمي للعام", null=False, blank=False)
    achievetest = models.FloatField(verbose_name="درجه اختبار التحصيلي", null=False, blank=False)
    area = models.CharField(max_length=255, verbose_name="المنطقه", null=False, blank=False)
    school = models.CharField(max_length=255, verbose_name="المدرسه", null=False, blank=False)
    highschooltype = models.CharField(max_length=255, verbose_name="نوع الثانويه العامه", null=False, blank=False)
    cognitivetest = models.FloatField(verbose_name="درجه اختبار القدرات", null=False, blank=False)

    # Other information
    mentionit = models.CharField(max_length=255, verbose_name="اذكرها", null=False, blank=False)
    certificate = models.CharField(max_length=255, verbose_name="اسم الشهاده", null=False, blank=False)
    college = models.CharField(max_length=255, verbose_name="الكليه", null=False, blank=False)
    gender = models.BooleanField(verbose_name="سبق ان التحقت بجامعه او كليه اخري", default=False, null=False, blank=False)
    gender_m = models.BooleanField(verbose_name="سبق ان حصلت علي شهاده جامعيه", default=False, null=False, blank=False)
    universityname = models.CharField(max_length=255, verbose_name="اسم الجامعه", null=False, blank=False)

    def __str__(self):
        return str(self.studentUser.username)
    





class UniversityData(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    student_email = models.EmailField()
    about_university = models.TextField()
    score1 = models.FloatField()
    score2 = models.FloatField()
    score3 = models.FloatField()
    score4 = models.FloatField()
    score5 = models.FloatField()
    score6 = models.FloatField()
    specialization1 = models.CharField(max_length=255)
    seats1 = models.IntegerField()
    college1 = models.CharField(max_length=255)
    acceptance_rate1 = models.FloatField()

    def __str__(self):
        return self.student_email

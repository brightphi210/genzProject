from django.db import models

from django.contrib.auth.models import UserManager, AbstractBaseUser, PermissionsMixin

from django.conf import settings

# Create your models here.


class CustomUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, **extra_fields)
    
# ======================== Creatives =============================
class User(AbstractBaseUser, PermissionsMixin):
    auto_id = models.PositiveBigIntegerField(
        unique=False, null=True, blank=True)
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    username = models.CharField(
        max_length=255, unique=True, blank=True, null=True)
    terms = models.BooleanField(default=False)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(null=True, blank=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name

    def save(self, *args, **kwargs):
        count_id = User.objects.all().count()
        self.auto_id = count_id+1
        super(User, self).save(*args, **kwargs)

    def _str_(self):
        return self.name
    

class UserProfile(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    profile_pic = models.ImageField(
        upload_to='profile_pics/', default='default.png', blank=True, null=True)

    def __str__(self):
        return self.user.email


# ====================== Authors ============================
class Authors(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(
        max_length=255, unique=True, blank=True, null=True)


    def __str__(self):
        return self.name
    
class AuthorsProfile(models.Model):
    author = models.ForeignKey(
        Authors, on_delete=models.CASCADE, null=True, blank=True)
    profile_pic = models.ImageField(
        upload_to='profile_pics/', default='default.png', blank=True, null=True)
    
    def __str__(self):
        return self.author.name
    

# ======================== Category ===============================
class Category(models.Model):
    name = models.CharField(max_length=225, blank=True, null=True)

    def __str__(self) :
        return self.name



# ======================= News ========================================


class News(models.Model):
    
    author = models.ForeignKey(Authors, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    title = models.CharField(max_length=225, blank=True, null=True)
    intro = models.TextField()
    body = models.TextField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.title
    

class Stories(models.Model):
    
    author = models.ForeignKey(Authors, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    title = models.CharField(max_length=225, blank=True, null=True)
    intro = models.TextField()
    body = models.TextField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.title


class MagazineStories(models.Model):
    
    author = models.ForeignKey(Authors, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    title = models.CharField(max_length=225, blank=True, null=True)
    intro = models.TextField()
    body = models.TextField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.title
    

class NewsLetter(models.Model):
    email = models.EmailField(max_length=255, null=True, blank= True)
    subscribed = models.BooleanField(default=False)
    subscribed_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Subcrition for {self.user.email}"
    




class SubscriptionPlan(models.Model):
    CATEGORY_CHOICES = [
        ('MONTHLY', 'MONTHLY'),
        ('A YEAR', 'A YEAR'),
        ('A YEAR WITH PRINT', 'A YEAR WITH PRINT'),
        # Add more category choices as needed
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    start_date = models.DateField()
    end_date = models.DateField()
    payment_status = models.BooleanField(default=False)

    def __str__(self):
        return self.category


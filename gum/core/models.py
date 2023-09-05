from django.db import models
from django.contrib.auth.models import User
import uuid
from django.utils.text import slugify

# Create your models here.


def user_directory_path(instance, filename):
    # Assuming you are using Django's authentication system and the connected user is available via the 'owner' field
    user = instance.item.owner
    # Generate a unique filename by appending a timestamp or using other logic if needed
    unique_filename = generate_unique_filename(filename)
    # Return the upload path in the format 'user_product_images/username/filename'
    return f'user_product_images/{user.username}/images/{unique_filename}'


def user_directory_path_job(instance, filename):
    # Assuming you are using Django's authentication system and the connected user is available via the 'owner' field
    user = instance.owner
    # Generate a unique filename by appending a timestamp or using other logic if needed
    unique_filename = generate_unique_filename(filename)
    # Return the upload path in the format 'user_product_images/username/filename'
    return f'user_product_images/{user.username}/images/{unique_filename}'



def generate_unique_filename(filename):
    # Generate a unique UUID
    unique_id = uuid.uuid4()
    # Get the file extension from the original filename
    file_extension = filename.split('.')[-1]
    # Concatenate the UUID and file extension to create a unique filename
    unique_filename = f'{unique_id}.{file_extension}'
    return unique_filename



class PhoneNumber(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, default=None)
    phone_number = models.CharField(max_length=20) 

    def __str__(self):
        return self.phone_number

class Category_job(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Job catégorie"
    
    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Catégorie"

    def __str__(self):
        return self.name

class Subcategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Sous-catégorie"

    def __str__(self):
        return self.name


class Type(models.Model):
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, default=None )
    name = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = "Type bien"

    def __str__(self):
        sub = str(self.subcategory)
        return sub + " " + self.name

class Ad(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    title = models.CharField(max_length=100, null=False, blank=False, default=None)
    date = models.DateTimeField(null=True, blank=True, auto_now_add=True)
    description = models.TextField(null=False, blank=False, default=None)
    available = models.BooleanField(default=True)
    class Meta:
        verbose_name = "Annonce"

    def __str__(self):
        return self.title 
    
    @property
    def available_string(self):
        if self.available:
            return "Disponible"
        return "Non disponible"

class Item(Ad):
    price = models.IntegerField(null=False, blank=False, default=None)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=None, blank=True, null=True)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.PROTECT, default=None, blank=True, null=True)
    type = models.ForeignKey(Type, on_delete=models.CASCADE, default=None)
    characteristics_item = models.ManyToManyField('Characteristics', through='Item_Characteristics')
    slug = models.SlugField(max_length=500, blank=True)
    primary_image = models.ImageField(upload_to=user_directory_path, default=None, blank=True, null=True)

    def save(self, *args, **kwargs):
        # Create the slug from the title when the model is saved
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Produit"
    
    def __str__(self):
        return self.title 
    
class ImageModel(models.Model):

    item = models.ForeignKey(Item, on_delete=models.CASCADE, default=None)
    image = models.ImageField(upload_to=user_directory_path)

    class Meta:
        verbose_name = "Product image"

    def __str__(self):
        return f'{self.item.owner.username} - {self.item.title}'

class Job(Ad):
    category = models.ForeignKey(Category_job, on_delete=models.CASCADE, default=None)
    salary = models.CharField(max_length=100, null=False, blank=False, default=None)
    type = models.CharField(max_length=100, default=None)
    heures = models.CharField(max_length=100, default=None)
    langues = models.ManyToManyField('Languages', default=None, blank=True)
    website = models.CharField(max_length=200, blank=True, null=True, default=None)
    characteristics_job = models.ManyToManyField('Characteristics', through='Job_Characteristics')
    job_logo = models.ImageField(upload_to=user_directory_path_job, null=True, blank=True, default=None)
    contract_type = models.CharField(max_length=100, default=None)
    niveau = models.ManyToManyField('Niveau', default=None, blank=True)
    period = models.DateField(default=None, null=True, blank=True)
    slug = models.SlugField(max_length=500, blank=True)

    def save(self, *args, **kwargs):
        # Create the slug from the title when the model is saved
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Job"
    
    def __str__(self):
        return self.title 

class Languages(models.Model):
    name = models.CharField(max_length=100, default=None)

    class Meta:
        verbose_name = "Langue"
    
    def __str__(self):
        return self.name

class Niveau(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Niveau"

    def __str__(self):
        return self.name

class Characteristics(models.Model):
    name = models.CharField(max_length=100, default=None)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, default=None)

    STRING = 'string'
    BOOLEAN = 'boolean'
    INTEGER = 'integer'

    VALUE_TYPES = (
        (STRING, 'String'),
        (BOOLEAN, 'Boolean'),
        (INTEGER, 'Integer'),
        # Add more types if needed.
    )

    type = models.CharField(max_length=10, choices=VALUE_TYPES, default=STRING)


    class Meta:
        verbose_name = "Caractéristique"
    
    def __str__(self):
        return self.name

class Item_Characteristics(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, default=None)
    characteristics = models.ForeignKey(Characteristics, on_delete=models.CASCADE, default=None)
    value = models.CharField(max_length=100)


    class Meta:
        verbose_name = "Characteristique produit"

    def __str__(self):

        sub = str(self.characteristics)
        return sub + " " + self.value

class Job_Characteristics(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, default=None)
    characterictics = models.ForeignKey(Characteristics, on_delete=models.CASCADE, default=None)
    value = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Characteristique job"

    def __str__(self):

        return self.value

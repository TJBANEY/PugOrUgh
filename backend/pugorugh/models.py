from django.contrib.auth.models import User
from django.db import models

dog_genders = (
    ('m', 'male'),
    ('f', 'female'),
    ('u', 'unknown')
)

status = (
    ('l', 'liked'),
    ('d', 'disliked')
)

age = (
    ('b', 'baby'),
    ('y', 'young'),
    ('a', 'adult'),
    ('s', 'senior')
)

gender = (
    ('m', 'male'),
    ('f', 'female')
)

size = (
    ('s', 'small'),
    ('m', 'medium'),
    ('l', 'large'),
    ('xl', 'extra large')
)

class Dog(models.Model):
    name = models.CharField(max_length=255)
    image_filename = models.ImageField()
    breed = models.CharField(max_length=255)
    age = models.IntegerField(default=1)
    gender = models.CharField(max_length=255, choices=dog_genders)

    def __str__(self):
        return self.name

class UserDog(models.Model):
    user = models.ForeignKey(User)
    dog = models.ForeignKey(Dog)
    status = models.CharField(max_length=255, choices=status)

    def __str__(self):
        return "{} - {}".format(self.user.email, self.dog.name)

class UserPref(models.Model):
    user = models.ForeignKey(User)
    age = models.CharField(max_length=255, choices=age)
    gender = models.CharField(max_length=255, choices=gender)
    size = models.CharField(max_length=255, choices=size)

    def __str__(self):
        return "{} - preferences".format(self.user.email, )
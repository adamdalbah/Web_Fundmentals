from django.db import models
import re

class UserManager(models.Manager):
    def validator(self, postD):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(postD['fname']) < 2:
            errors['fname'] = "First name should be at least 2 characters"
        
        if len(postD['lname']) < 2:
            errors['lname'] = "Last name should be at least 2 characters"
        
        if not EMAIL_REGEX.match(postD['email']):
            errors['email'] = "Invalid email address!"
        
        if postD['password'] != postD['cpassword']:
            errors['password_matching'] = "Passwords should match"
        
        if len(postD['password']) < 8:
            errors['password'] = "Password should be at least 8 characters"
        
        return errors

    def login_validator(self, postD):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postD['email']):
            errors['email'] = "Invalid email address!"

        if len(postD['password']) < 8:
            errors['password'] = "Password should be at least 8 characters"
        
        return errors        

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password= models.CharField(max_length=255)
    cpassword= models.CharField(max_length=255)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    objects = UserManager()
# Create your models here.

def register(fname, lname, email, passwd, cpasswd):
    User.objects.create(first_name = fname, last_name= lname, email = email,
    password = passwd, cpassword = cpasswd)
    print(User.objects.all())

def check_user(email, passwd):
    user_name = User.objects.filter(email=email)
    if user_name == None:
        return False
    
    if user_name.first().password == passwd:
        return True
    return False

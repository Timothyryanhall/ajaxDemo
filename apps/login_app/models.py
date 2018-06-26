from __future__ import unicode_literals
from django.db import models
from datetime import datetime
import re

# class User(models.Model):
#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)
#     email = models.CharField(max_length=255)
#     age = models.IntegerField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     objects = UserManager()

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9+-_.]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def register_validator(self, postData):
        errors = {}
        
        if len(postData['first']) < 1:
            errors['first_name'] = "First name is required"
        elif len(postData['first']) < 2:
            errors['first_name'] = "First name must have be at least 2 characters long"
        
        if len(postData['last']) < 1:
            errors['last_name'] = "Last name is required"
        elif len(postData['last']) < 2:
            errors['last_name'] = "Last name must have be at least 2 characters long"
        
        if len(postData['email']) < 1:
            errors['email'] = "Email is required"
        elif not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid Email"
        else:
            list_of_users_matching_email = User.objects.filter(email=postData["email"].lower())
            if len(list_of_users_matching_email) > 0:
                errors['email'] = "Email already registered"

        # if len(postData['date_of_birth']) < 1:
        #     errors['date_of_birth'] = "Date of Birth is required"
        # else:
        #     dob = datetime.strptime(postData["date_of_birth"], "%Y-%m-%d")
        #     if dob > datetime.now():
        #         errors['date_of_birth'] = "Date of Birth must be in the past"

        # if len(postData['password']) < 1:
        #     errors['password'] = "Password is required"
        # elif len(postData['password']) < 8:
        #     errors['password'] = "Password must be at least 8 characters long"
        
        # if len(postData["confirm"]) < 1:
        #     errors['confirm'] = "Confirm password is required"
        # elif postData["password"] != postData["confirm"]:
        #     errors['confirm'] = "Confirm password must match Password"
            
        return errors
    
    def login_validator(self, postData):
        response = {
            "errors": [],
            "is_valid": True,
            "user": None
        }

        if len(postData['email']) < 1:
            response['errors'].append("Email is required")
        elif not EMAIL_REGEX.match(postData['email']):
            response['errors'].append("Invalid Email")
        else:
            list_of_users_matching_email = User.objects.filter(email=postData["email"].lower())
            if len(list_of_users_matching_email) == 0:
                response['errors'].append("Email not registered")
        
        # if len(postData['password']) < 1:
        #     response['errors'].append("Password is required")
        # elif len(postData['password']) < 8:
        #     response['errors'].append("Password must be at least 8 characters long")
        # else:
            else: 
                user = list_of_users_matching_email[0]
            # if bcrypt.checkpw(postData['password'].encode(), user.password.encode()):
                response['user'] = user
            # else:
            #     response['errors'].append("Incorrect password")
        
        if len(response["errors"]) > 0:
            response["is_valid"] = False
        
        return response

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()